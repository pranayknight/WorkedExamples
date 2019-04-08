import logging

logging.basicConfig(filename="mylog.log",level=logging.DEBUG)   # this logs the error in file specified , and depending on the level of logging used they are logged themselves above the one that is used in the level into the file

logging.critical("Critical")
logging.error("error")
logging.warning("Warning")
logging.info("Info")
logging.debug("Debug")
