import logging
import traceback

from flask import jsonify


def configure_logger():
    logging.basicConfig(filename='error_logs.txt', level=logging.ERROR,
                        format='%(asctime)s %(levelname)s %(name)s %(message)s')
    logger = logging.getLogger(__name__)
    return logger


def error_logger(logger, e):
    # Log the error
    logger.error(f'Error occurred: {e}')
    logger.error(traceback.format_exc())
    # Return error message as JSON
    return jsonify({'error': str(e), 'trace': traceback.format_exc()}), 500
