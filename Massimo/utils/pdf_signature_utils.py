from pathlib import Path

class PdfSignatureUtils:
    """Utility class for pdf signature processing"""

    def __init__(self, pdf_dir: str):
        directory_path = Path(pdf_dir)

        if not directory_path.exists():
            raise FileNotFoundError(f"Directory not found: {pdf_dir}.")

        if not directory_path.is_dir():
            raise ValueError(f"Path is not a directory: {pdf_dir}.")

        self._directory_path = directory_path

