import logging


def init_logging(app_logfilename):
  logging.basicConfig(filename=app_logfilename,format='%(asctime)s|%(process)-5d|%(thread)d|%(filename)-30s|%(funcName)-16s|%(lineno)4d|%(levelname)-8s| %(message)s', level=logging.DEBUG)


#adding more code
