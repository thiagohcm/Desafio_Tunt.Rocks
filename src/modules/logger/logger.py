import logging
import os


def setup_logger():
    logger = logging.getLogger()
    # set log level
    logger.setLevel(logging.INFO)

    # define handler and formatter
    handler = logging.FileHandler(os.path.join('logs', 'app.log'))
    # handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s - %(message)s")

    # add formatter to handler
    handler.setFormatter(formatter)

    # add handler to logger
    logger.addHandler(handler)
