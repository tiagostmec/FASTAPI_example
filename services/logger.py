import logging
import logging.config
import json
import pathlib
import os 

project_dir = pathlib.Path(__file__).resolve().parent.parent
config_file = project_dir / "services" / "logger_config.json"

with open(config_file) as f_in:
    config = json.load(f_in)

for handler_config in config.get("handlers", {}).values():
    if "filename" in handler_config:
        log_file_path = pathlib.Path(handler_config["filename"])
        log_file_dir = log_file_path.parent
        log_file_dir.mkdir(parents=True, exist_ok=True)

logging.config.dictConfig(config)
logging.basicConfig(level=logging.NOTSET)

logger = logging.getLogger()