"""Tutorial for python loggings

Owner: Kyeongmin Woo
Email: wgm0601@gmail.com

References:
    - Logging HOWTO: https://docs.python.org/3/howto/logging.html
"""
import os
import argparse
import logging

from logger import external_logger


def five_log_levels():
    """Show 5 log levels: DEBUG(10), INFO(20), WARNING(30), ERROR(40), CRITICAL(50).
    
    Printed Log:
        WARNING:root:This is warning
        ERROR:root:This is error
        CRITICAL:root:This is critical
    """
    # logs
    logging.debug("This is debug")
    logging.info("This is info")
    logging.warning("This is warning")
    logging.error("This is error")
    logging.critical("This is critical")

def change_log_level():
    """Set log level as logging.DEBUG -> It print debug and info too.
    
    Printed Log:
        DEBUG:root:This is debug
        INFO:root:This is info
        WARNING:root:This is warning
        ERROR:root:This is error
        CRITICAL:root:This is critical
    """
    logging.basicConfig(level=logging.DEBUG)
    # logs
    logging.debug("This is debug")
    logging.info("This is info")
    logging.warning("This is warning")
    logging.error("This is error")
    logging.critical("This is critical")

def store_log():
    """Store log at the file name ./log/store_log.log
    
    Notes:
        - with filename parameter, it does not print any log directly.
    """
    # settings for log file
    logging.basicConfig(filename='./logs/store_log.log', level=logging.DEBUG)

    # logs
    logging.debug("This is debug")
    logging.info("This is info")
    logging.warning("This is warning")
    logging.error("This is error")

def use_format():
    """Set format of the logging.
    
    Printed Log:
        2021/04/04 12:35:43 [DEBUG] This is debug
        2021/04/04 12:35:43 [INFO] This is info
        2021/04/04 12:35:43 [WARNING] This is warning
        2021/04/04 12:35:43 [ERROR] This is error
    """
    # settings for log file
    logging.basicConfig(
        format='%(asctime)s [%(levelname)s] %(message)s', 
        level=logging.DEBUG, 
        datefmt='%Y/%m/%d %I:%M:%S'
    )

    # logs
    logging.debug("This is debug")
    logging.info("This is info")
    logging.warning("This is warning")
    logging.error("This is error")

def use_external_logger():
    """Execute function defined at external module with logging.
   
   Printed Log:
        WARNING:root:This is internal logger
        WARNING:root:This is external logger
    """
    logging.warning("This is internal logger")
    external_logger()  # logging.warning("This is external logger")

def save_and_print_together():
    """Set logger to save log and print it together.
        
    References:
        - StackOverflow: https://bit.ly/3wjvaXs

    Printed Log:
        This is debug
        This is info
        This is warning
        This is error

    Saved Log(save_and_print.log):
        DEBUG:root:This is debug
        INFO:root:This is info
        WARNING:root:This is warning
        ERROR:root:This is error
    """
    logging.basicConfig(filename='./logs/save_and_print.log', level=logging.DEBUG)
    logging.getLogger().addHandler(logging.StreamHandler())
    # logs
    logging.debug("This is debug")
    logging.info("This is info")
    logging.warning("This is warning")
    logging.error("This is error")



# parser
parser = argparse.ArgumentParser()
parser.add_argument("--func", type=str, default="five_log_levels", help="Define the function to run")
args = parser.parse_args()

if __name__ == "__main__":
    
    if not os.path.exists("./logs"):
        os.mkdir("./logs")

    func = locals().get(args.func)
    if func:
        func()
    else:
        raise NotImplementedError()
