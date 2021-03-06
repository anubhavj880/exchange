import datetime
import logging
logging.basicConfig()


def getLogger(loggerName='test', logLevel='INFO'):
    class Formatter(logging.Formatter):
        def formatTime(self, record, datefmt=None):
            return (datetime.datetime.now()).strftime('%H:%M:%S')
    logLevel = logLevel.upper()
    levels = {'DEBUG'   : logging.DEBUG,
            'INFO'      : logging.INFO,
            'WARNING'   : logging.WARNING,
            'ERROR'     : logging.ERROR,
            'CRITICAL'  : logging.CRITICAL}
    logger = logging.getLogger(loggerName)
    if not len(logger.handlers):
        logger.setLevel(levels[logLevel])
        log_path = r'F:/upwork/Bitmex/binance_log.txt'
        fh = logging.FileHandler(log_path)
        formatter = Formatter('%(asctime)s.%(msecs)03d - %(levelname)s - [ %(message)s ] - (%(filename)s:%(lineno)s||T=%(thread)d)', datefmt='%H:%M:%S')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        logger.propagate = False
        logger.info('loggerName: %s' % loggerName)
    return logger




