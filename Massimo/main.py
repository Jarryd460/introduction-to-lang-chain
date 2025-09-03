from config import Config
from pathlib import Path
from utils import *

def main():
    file_name_2 = "PublicWaterMassMailing.pdf"

    # Load .env into env variables
    Config()

    root = Path.cwd()
    pdf_dir = (root / "data").resolve()

    pdf_text_utils = PdfTextUtils(str(pdf_dir))

    document = pdf_text_utils.extract_text(file_name_2)

    print(document)

if __name__ == '__main__':
    main()