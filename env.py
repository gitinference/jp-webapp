from dotenv import load_dotenv
import os

load_dotenv()


# Get the Database credentials
def get_db_credentials() -> list:
    USER = str(os.environ.get("POSTGRES_USER")).strip()
    HOST = str(os.getenv("POSTGRES_HOST")).strip()
    PORT = str(os.environ.get("POSTGRES_PORT")).strip()
    DATABASE = str(os.environ.get("POSTGRES_DB")).strip()
    PASSWORD = str(os.getenv("POSTGRES_PASSWORD")).strip()
    SECRET_KEY = str(os.getenv("SECRET_KEY")).strip()
    DEBUG = os.getenv("DEBUG")

    if not all([HOST, USER, DATABASE, SECRET_KEY, PORT, PASSWORD]):
        raise ValueError("Database credentials not set")
    if os.environ.get("DEV") == "True":
        HOST = "localhost"
        DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
        API_URL = str(os.getenv("API_URL")).strip()
    else:
        HOST = "postgres"
        DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
        API_URL = "FastAPI"
    return [
        USER,
        PASSWORD,
        HOST,
        DATABASE,
        DATABASE_URL,
        SECRET_KEY,
        API_URL,
        PORT,
        DEBUG,
    ]
