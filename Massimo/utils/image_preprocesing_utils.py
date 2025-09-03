import cv2

# This preprocessing is tailored to black & white document pdfs

class ImagePreprocessingUtils:
    """Utility class for image preprocessing"""

    @staticmethod
    def process_image_for_ocr(image_arr):
        """Enhance image quality before OCR"""

        # Apply adaptive thresholding for better contrast. Might be necessary for poor confidence OCR.
        return cv2.adaptiveThreshold(
            image_arr,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            11,
            2
        )