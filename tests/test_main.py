import json
import pytest

from pathlib import Path
from unittest.mock import patch

from main import create_logs_folder, setup_logging


@pytest.fixture
def mock_logs_dir(tmp_path):
    test_dir = tmp_path / "logs"
    return test_dir


def test_create_logs_folder(monkeypatch, mock_logs_dir):
    """Test the create_logs_folder function."""
    monkeypatch.setattr(
        "main.Path", lambda path: mock_logs_dir if path == "logs" else Path(path)
    )

    assert not mock_logs_dir.exists()

    create_logs_folder()

    assert mock_logs_dir.exists()


@pytest.fixture
def mock_config_file(tmp_path):
    """Fixture to create a temporary logging configuration file."""
    config_content = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {"simple": {"format": "%(levelname)s: %(message)s"}},
        "handlers": {
            "stderr": {
                "class": "logging.StreamHandler",
                "level": "WARNING",
                "formatter": "simple",
                "stream": "ext://sys.stderr",
            }
        },
        "loggers": {"root": {"level": "DEBUG", "handlers": ["stderr"]}},
    }

    config_path = tmp_path / "logging_config.json"
    with open(config_path, "w") as f:
        json.dump(config_content, f)

    return config_path


def test_setup_logging(mock_config_file):
    """Test the setup_logging function."""
    with (
        patch("main.create_logs_folder") as mock_create_logs_folder,
        patch("main.Path") as mock_path,
        patch("main.logging.config.dictConfig") as mock_dict_config,
    ):
        mock_path.return_value = mock_config_file

        setup_logging()

        mock_create_logs_folder.assert_called_once()

        mock_path.assert_called_once_with("logging_configs/logging_config.json")

        with open(mock_config_file) as cfg:
            expected_config = json.load(cfg)
        mock_dict_config.assert_called_once_with(config=expected_config)
