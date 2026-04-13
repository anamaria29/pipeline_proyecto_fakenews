import logging
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "orchestrator.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


def run_step(script_name: str) -> None:
    script_path = BASE_DIR / "scripts" / script_name
    logger.info("Ejecutando %s", script_name)
    result = subprocess.run([sys.executable, str(script_path)], cwd=BASE_DIR)
    if result.returncode != 0:
        raise RuntimeError(f"Falló la ejecución de {script_name}")


def main() -> None:
    logger.info("Iniciando pipeline")
    run_step("etl_fakenews.py")
    run_step("validate_pipeline.py")
    logger.info("Pipeline ejecutado")


if __name__ == "__main__":
    main()
