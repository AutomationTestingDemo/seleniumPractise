import logging
logging.basicConfig(filename="file.log",format='%(asctime)s: %(levelname)s: %(message)s',level=logging.DEBUG)

# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)
logging.debug("This is debug")
logging.critical("This is critical")
logging.error("this is error")
logging.info("this is info")
logging.warning("this is warning")

#log file will not show debug and info logs as they are below threshold point
#but to make debug and info logs print to log file add level= logging.DEBUG as parementer in basicConfig

# Log Levels:
# debug
# info
# warning
# critical
# error