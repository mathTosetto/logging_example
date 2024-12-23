import json
import logging.config
import logging.handlers

from pathlib import Path

logger = logging.getLogger("my_app")


def setup_logging():
    create_logs_folder()

    config_file = Path("logging_configs/logging_config.json")
    with open(config_file) as cfg:
        config = json.load(cfg)
    logging.config.dictConfig(config=config)


def create_logs_folder():
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)


def main():
    setup_logging()
    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("Error message")
    logger.critical("Critical message")
    try:
        1 / 0
    except ZeroDivisionError:
        logger.exception("Exception message")


if __name__ == "__main__":
    main()
