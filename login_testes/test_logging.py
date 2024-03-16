#loggings are used to capture the details
#to warn
#to give info
#for critical errors
#we can write pytest.ini file 
import logging
def test_logging():
    Logger=logging.getLogger(__name__)
    Logger.info("this is information logs")
    Logger.warning("this is warning")
    Logger.critical("this is critical")