import os
from copy import deepcopy

from core.settings import BASE_DIR

from loguru import logger as log

LOGS_DIR = os.path.join(BASE_DIR, 'logs')

if not os.path.exists(LOGS_DIR):
    os.mkdir(LOGS_DIR)

ROTATION = '1 month'
RETENTION = '6 month'


class Logging:
    _logger = None

    @staticmethod
    def set_logger(
            logger_,
            filename,
            rotation=ROTATION,
            retention=RETENTION,
            compression=True
    ):
        logger_.add(
            os.path.join(BASE_DIR, f'{filename}.log'),
            rotation=rotation,
            retention=retention,
            compression='zip' if compression else None,
        )

        return logger_


log.remove()

logger = Logging.set_logger(deepcopy(log), 'base')
