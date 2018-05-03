import time
from utils.log import Logger

logger = Logger("log_test")

if __name__ == "__main__":
    while True:
        time.sleep(3)
        logger.debug("TEST FORM LOGGER! %s" % int(time.time()))
