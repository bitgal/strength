from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
FOR_MYSQL_DIR = DATA_DIR / "for_mysql"
IMAGES_DIR = RAW_DATA_DIR / "images"
