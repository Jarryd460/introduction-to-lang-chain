from dotenv import load_dotenv

class Config:
    """Load .env into environment variables"""

    def __init__(self):
        load_dotenv()