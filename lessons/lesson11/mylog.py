import logging


logging.basicConfig(level=logging.ERROR,
                    filemode="w",
                    filename='lessons\\lesson11\\log.log',
                    format='%(process)d %(asctime)s %(filename)s %(funcName)s %(name)s - %(levelname)s - %(message)s')


logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')