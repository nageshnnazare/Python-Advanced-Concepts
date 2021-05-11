#Logging Basics:

"""
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""

# from logging import root
import logging

def test():
    print('-'*25)
    level = logging.getLevelName(logging.getLogger().getEffectiveLevel())
    print(f'Log Level : {level}')
    logging.debug('Debug Message')
    logging.info('Info Message')
    logging.warning('Warning Message')
    logging.error('Error Message')
    logging.critical('Critical Message')
    print('-'*25)

test()

#logging levels

#Get the root logger
rootlog = logging.getLogger()
print('Level ' + logging.getLevelName(rootlog.getEffectiveLevel()))

#Set it to DEBUG
rootlog.setLevel(logging.DEBUG)
test()

#Set it to CRITICAL
rootlog.setLevel(logging.CRITICAL)
test()

# Log to a File
handler = logging.FileHandler('file.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler.setFormatter(formatter)
rootlog.addHandler(handler)
rootlog.setLevel(logging.DEBUG)
rootlog.debug("test")
test()