import logging
from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine, text

DB_URL = "postgresql://postgres:Sagitario129!@localhost/postgres"
SOURCE_TABLE = "noticias"
TARGET_TABLE = "noticias_curadas"

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "etl.log"

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
    logger.info("Iniciando ETL")
    engine = create_engine(DB_URL)

    logger.info("extrayendo datos desde la tabla %s", SOURCE_TABLE)
    df = pd.read_sql(f"SELECT * FROM {SOURCE_TABLE}", engine)
    logger.info("Filas extraídas: %s", len(df))

    logger.info("impieza y transformacion")
    df = df.dropna(subset=["title", "text"])
    df["title"] = df["title"].astype(str).str.strip()
    df["text"] = df["text"].astype(str).str.strip()
    df["subject"] = df["subject"].astype(str).str.strip().str.lower()
    df = df.drop_duplicates(subset=["title", "text"])

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date"])
    df["date"] = df["date"].dt.date

    df["title_length"] = df["title"].str.len()
    df["text_length"] = df["text"].str.len()
    df["word_count"] = df["text"].apply(lambda x: len(str(x).split()))

    logger.info("filas despues de transformacion: %s", len(df))

    with engine.begin() as connection:
        connection.execute(text(f"DROP TABLE IF EXISTS {TARGET_TABLE}"))

    logger.info("Cargando datos en la tabla %s", TARGET_TABLE)
    df.to_sql(TARGET_TABLE, engine, if_exists="replace", index=False)

    logger.info("ETL completado")
    logger.info("Columnas finales: %s", list(df.columns))


if __name__ == "__main__":
    main()
