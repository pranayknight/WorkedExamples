import logging

logging.basicConfig(filename="/home/pranay/Documents/SeleniumRelatedFiles/test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%y %I:%M:%S %p')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("This is a debug message")
logger.info("This is a info message")
logger.warning("This is a warning message")
logger.error("This is an Error message")
logger.critical("This is a Critical message")