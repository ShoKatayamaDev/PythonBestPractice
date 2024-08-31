""" logging manner """

from logging import getLogger, StreamHandler, FileHandler, Formatter, DEBUG


def main():
    ''' main function '''
    # do not use logging(=root logger). use local logger instead.
    logger = getLogger(__name__)
    # set handler
    # log level is DEBUG which means all logs above DEBUG will be OUTPUT
    handler = StreamHandler()
    handler.setLevel(DEBUG)
    # optional: set another handler
    handler2 = FileHandler('my.log')
    handler2.setLevel(DEBUG)
    # optional: set log format
    formatter = Formatter(
        '[%(levelname)s] @%(name)s : %(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    handler2.setFormatter(formatter)
    # set log level
    # log level is DEBUG which means all logs above DEBUG will be CREATED
    logger.setLevel(DEBUG)
    # add handler
    logger.addHandler(handler)
    logger.addHandler(handler2)
    # set propagate to False so that logs are not propagated to root logger
    logger.propagate = False

    logger.debug('debug message')
    logger.info('info message')


if __name__ == '__main__':
    main()
