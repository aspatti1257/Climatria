import logging
import sys


class LoggerFactory:

    @staticmethod
    def create_log(clazz):
        log = logging.getLogger(clazz)
        log.setLevel(logging.INFO)

        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
        handler.setFormatter(formatter)
        log.addHandler(handler)

        return log
