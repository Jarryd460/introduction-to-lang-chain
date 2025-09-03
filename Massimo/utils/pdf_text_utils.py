import numpy as np
import pymupdf

from pathlib import Path
from paddleocr import PaddleOCR

class PdfTextUtils:
    """Utility class for pdf text processing"""

    def __init__(self, pdf_dir: str):
        directory_path = Path(pdf_dir)

        if not directory_path.exists():
            raise FileNotFoundError(f"Directory not found: {pdf_dir}.")

        if not directory_path.is_dir():
            raise ValueError(f"Path is not a directory: {pdf_dir}.")

        self._directory_path = directory_path
        self._ocr = PaddleOCR(
            lang='en',
            text_detection_model_name="PP-OCRv5_server_det",
            text_recognition_model_name="PP-OCRv5_server_rec",
            use_doc_orientation_classify=True,
            use_doc_unwarping=False,
            use_textline_orientation=True
        )

    def extract_text(self, file_name: str) -> str:
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

    def _extract_text_from_ocr(self, page) -> tuple[str, float]:
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

        ocr_result = self._ocr.predict(img_array)

        for res in ocr_result:
            # res.print()
            res.save_to_img("output")
            # res.save_to_json("output")

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