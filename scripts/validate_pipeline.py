import logging
from pathlib import Path

from sqlalchemy import create_engine, text

DB_URL = "postgresql://postgres:Sagitario129!@localhost/postgres"
TARGET_TABLE = "noticias_curadas"

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "validation.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


def main() -> None:
    logger.info("Iniciando validacion")
    engine = create_engine(DB_URL)

    with engine.connect() as connection:
        count = connection.execute(text(f"SELECT COUNT(*) FROM {TARGET_TABLE}"))
        total_rows = count.scalar()

        null_titles = connection.execute(
            text(f"SELECT COUNT(*) FROM {TARGET_TABLE} WHERE title IS NULL OR TRIM(title) = ''")
        ).scalar()

        null_texts = connection.execute(
            text(f"SELECT COUNT(*) FROM {TARGET_TABLE} WHERE text IS NULL OR TRIM(text) = ''")
        ).scalar()

    logger.info("Filas en tabla curada: %s", total_rows)
    logger.info("Titulos nulos o vacios: %s", null_titles)
    logger.info("Textos nulos o vacíos: %s", null_texts)

    if total_rows > 0:
        if null_titles > 0:
            logger.warning("Advertencia: hay %s titulos nulos o vacios", null_titles)
        if null_texts > 0:
            logger.warning("Advertencia: hay %s textos nulos o vacios", null_texts)
        logger.info("Validacion completada")
    else:
        raise ValueError("validacion fallo: la tabla curada esta vacia.")


if __name__ == "__main__":
    main()
