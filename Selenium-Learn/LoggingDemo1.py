import logging

logging.basicConfig(filename="/home/pranay/Documents/SeleniumRelatedFiles/test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%y %I:%M:%S %p',
                    level=logging.DEBUG)


logging.debug("This is a debug message")
logging.info("This is a info message")
logging.warning("This is a warning message")
logging.error("This is an Error message")
logging.critical("This is a Critical message")
