import logging
import os

def get_logger(name):
    os.makedirs("reports", exist_ok=True)
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        fh = logging.FileHandler("reports/test.log")
        fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        fh.setFormatter(fmt)
        logger.addHandler(fh)
    return logger