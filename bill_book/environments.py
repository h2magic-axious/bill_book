import os

import dotenv

dotenv.load_dotenv()


class Env:
    DEBUG = os.getenv("DEBUG", "TRUE") == "TRUE"
    DB_PORT = os.getenv("DB_PORT", 5432)
    DB_HOST = os.getenv("DB_HOST", "127.0.0.1")

    ADMIN_USER = os.getenv("ADMIN_USER")
    ADMIN_PASS = os.getenv("ADMIN_PASS")
