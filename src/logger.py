import os
import logging
import logging.config

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Python logger configuration
# Where to store the logfile. Default: PROJECT_PATH/sauron.log
LOGFILE = '/tmp/octodon.log'
LOG_CONFIG = {
    "version": 1,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(filename)s->%(funcName)s:%(lineno)s] %(message)s",
            'datefmt': "%Y/%m/%d %H:%M:%S"
        },
    },
    'handlers': {
        'logfile': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOGFILE,
            'maxBytes': 10485760,  # 10MB per file
            'backupCount': 2,  # Store up to three files
            'formatter': 'standard',
        }
    },
    'loggers': {
        'ek-sauron': {
            'handlers': ["logfile", ],
            'level': 'DEBUG',
        },
    }
}

logging.config.dictConfig(LOG_CONFIG)
logger = logging.getLogger("octodon")
logger.info('Logging ready.')
