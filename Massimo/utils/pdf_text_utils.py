import cv2
import numpy as np
import pymupdf

from enum import Enum
from pathlib import Path
from paddleocr import PaddleOCR

from .image_preprocesing_utils import ImagePreprocessingUtils

class PdfTextUtils:
    """Utility class for pdf text processing"""

    def __init__(self, pdf_dir: str):
        directory_path = Path(pdf_dir)

        if not directory_path.exists():
            raise FileNotFoundError(f"Directory not found: {pdf_dir}.")

        if not directory_path.is_dir():
            raise ValueError(f"Path is not a directory: {pdf_dir}.")

        self._directory_path = directory_path
        self._image_preprocess = ImagePreprocessingUtils()
        self._ocr = PaddleOCR(
            lang='en',
            ocr_version="PP-OCRv5",

            # Detection parameters - more aggressive text region detection
            text_det_thresh=0.1,  # Lower threshold to detect more text regions (default: 0.3)
            text_det_box_thresh=0.3,  # Lower box threshold for more sensitive detection (default: 0.6)
            text_det_unclip_ratio=2.0,  # Larger unclip ratio to expand detected regions (default: 1.5)
            text_det_limit_side_len=2560,  # Increase detection resolution (default: 960)
            text_det_limit_type='max',  # Use max side length limit

            # Recognition parameters - better accuracy
            text_rec_score_thresh=0.5,

            # Device/performance parameters
            device = 'cpu',  # or 'gpu'
            enable_mkldnn = True,  # Intel MKL-DNN acceleration
            cpu_threads = 4,  # Number of processes

            # Optional advanced parameters
            precision='fp32',  # or 'fp16', 'int8'
            use_tensorrt=False,  # TensorRT acceleration for GPU

            # Disable unless needed
            use_doc_orientation_classify=False,
            use_doc_unwarping=True,
            use_textline_orientation=True
        )

    def extract_text(self, file_name: str, min_confidence = 0.7) -> str:
        file_path = self._directory_path / file_name

        if not file_path.exists():
            raise FileNotFoundError(f"PDF file not found: {file_path}.")

        page_content = []
        with pymupdf.open(file_path) as document:
            for page in document:
                text = page.get_text().strip()

                if not self._needs_ocr(page, text):
                    page_content.append(text)
                else:
                    text, confidence = self._extract_text_from_ocr(page)

                    print(f"Page {page} confidence with normal execution: {confidence}")

                    if confidence > min_confidence:
                        page_content.append(text)
                        continue

                    text, confidence = self._extract_text_from_ocr(page, True)

                    print(f"Page {page} confidence with adaptive thresholding: {confidence}")

                    page_content.append(text)

        return  "\n".join(page_content)

    def _needs_ocr(self, page, text) -> bool:
        """
            Comprehensive check to determine if a PDF page needs OCR processing.

            Returns True if any of these conditions are met:
                - No extractable text exists on any page
                - Any page is completely covered by an image
                - Hundreds of small vector graphics (indicating simulated text)
        """

        """No extractable text exists on any page"""
        if len(text) == 0:
            return True

        """Check if page is mostly covered by large images"""
        if self._is_page_covered_by_image(page):
            return True

        """Hundreds of small vector graphics (indicating simulated text)"""
        if self._has_simulated_text_graphics(page):
            return True

        char_count = len(text)
        image_count = len(page.get_images())
        drawing_count = len(page.get_drawings())

        """More than 10 images/drawings per 100 characters suggests scanned content"""
        if char_count < 50 and (image_count + drawing_count) > 5:
            return True

        return False

    @staticmethod
    def _is_page_covered_by_image(page) -> bool:
        """Check if page is mostly covered by large images"""

        # Get page bounding rectangle
        page_area = page.rect.width * page.rect.height

        if page_area == 0:
            return False

        total_image_coverage = 0

        for image_index in page.get_images():
            try:
                # Get image bounding rectangle and add to total image coverage
                image_rect = page.get_image_rects(image_index[0])

                for rect in image_rect:
                    image_area = rect.width * rect.height
                    total_image_coverage += image_area
            except:
                # Handle corrupted/broken images gracefully
                continue

        # If images cover more than 80% of page area, consider it image-based
        return (total_image_coverage / page_area) > 0.8

    @staticmethod
    def _has_simulated_text_graphics(page) -> bool:
        """Detect if page has many small vector graphics that simulate text"""

        # Gets all vector graphics elements
        drawings = page.get_drawings()

        # Not enough drawings to be simulated text
        if len(drawings) < 100:
            return False

        small_drawing_count = 0

        for drawing in drawings:
          for item in drawing.get("items", []):
              # Look for character sized rectangles
              if item[0] == "re":
                  rect = item[1]
                  width = abs(rect.x1 - rect.x0)
                  height = abs(rect.y1 - rect.y0)

                  # Small rectangles that could be simulated characters
                  if 2 < width < 20 and 5 < height < 25:
                      small_drawing_count += 1

        # If more than 200 small drawings, likely simulated text
        return small_drawing_count > 200

    def _extract_text_from_ocr(self, page, preprocessing = False) -> tuple[str, float]:
        pixmap = page.get_pixmap(
            # 4x magnification for better OCR
            matrix=pymupdf.Matrix(4, 4),
            alpha=False,
            colorspace=pymupdf.csRGB
        )

        img_array = (
            np.frombuffer(pixmap.samples, dtype=np.uint8)
                .reshape(pixmap.height, pixmap.width, pixmap.n)
        )

        if preprocessing:
            img_array = self._image_preprocess.process_image_for_ocr(img_array)

        ocr_result = self._ocr.predict(img_array)

        if not ocr_result or not ocr_result[0]:
            return "", 0.0

        ocr_result = ocr_result[0]

        if 'rec_texts' in ocr_result:
            texts = ocr_result['rec_texts']
            text = "\n".join(texts)
        else:
            text = ""

        if 'rec_scores' in ocr_result:
            scores = ocr_result['rec_scores']
            avg_confidence = sum(scores) / len(scores) if scores else 0.0
        else:
            avg_confidence = 0.0

        return text, avg_confidence