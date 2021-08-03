import logging
import json
import os
from dotenv import load_dotenv

# basic configuration
# filemode  Specifies the mode to open the file, if filename is specified
#               (if filemode is unspecified, it defaults to 'a').

# Add time, level name and the message


load_dotenv()

# print('from file: ', os.environ.get('log-file'))
# log_to_file = (False, True)[os.environ.get('log-file') == 'True']
# print('logging to file {}'.format(log_to_file))
# output_log = None
#
# if log_to_file:
#     output_log = '.. / application_logs / output.log'
#     if not os.path.exists(output_log):
#         open(file=output_log)

logging.basicConfig(level=logging.DEBUG,
                    # filename=output_log,
                    format='%(asctime)s:%(levelname)s:%(message)s')

logger = logging.getLogger()
print('os.environ.enable-logging: ', os.environ.get('enable-logging'))
logger.disabled = (True, False)[os.environ.get('enable-logging') == 'True']  # (falseValue, trueValue)[test == True]
print('logger.disabled', logger.disabled)


def test():
    logger.debug("test message")


test()
