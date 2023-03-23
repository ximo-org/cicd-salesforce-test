'''Class for handling logging'''

# Libs
import logging, os
import datetime
import colorama

# Local imports
from options import LOGGING_LEVEL

## CLASSES
class BasicLogger(logging.Logger):
    '''Custom logger class with multiple destinations'''

    def __init__(self, name, level=logging.NOTSET):
        super().__init__(name, level)

        # Create formatters and handlers
        ff = logging.Formatter('%(asctime)s %(name)s:%(levelname)s %(module)s:%(lineno)d:  %(message)s')
        cf = ConsoleFormater()
        
        # File handler
        path_for_logs = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')
        if not os.path.exists(path_for_logs):
            os.mkdir(path_for_logs)
        fh = logging.FileHandler(os.path.join(path_for_logs, f'{datetime.date.today()}.txt'))
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(ff)

        # Console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(cf)

        # Add the handlers to the logger
        self.addHandler(fh)
        self.addHandler(ch)
        
        self.set_level()

    def set_level(self, level = None):
        if level is None:
            self.setLevel(LOGGING_LEVEL)
        else:
            self.setLevel(level)

    def process(self, msg, kwargs):
        return msg, kwargs

## FORMATTERS

class ConsoleFormater(logging.Formatter):
    '''Custom formater for console output'''

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        colorama.init()

    def format(self, record):
        # Get the original format
        result = logging.Formatter.format(self, record)
        # Add color
        if record.levelno == logging.DEBUG:
            result = colorama.Fore.CYAN + result + colorama.Fore.RESET
        elif record.levelno == logging.INFO:
            result = colorama.Fore.GREEN + result + colorama.Fore.RESET
        elif record.levelno == logging.WARNING:
            result = colorama.Fore.YELLOW + result + colorama.Fore.RESET
        elif record.levelno == logging.ERROR:
            result = colorama.Fore.RED + result + colorama.Fore.RESET
        elif record.levelno == logging.CRITICAL:
            result = colorama.Fore.RED + colorama.Back.WHITE + result + colorama.Fore.RESET + colorama.Back.RESET
        return result

## HANDLERS

## LOGGERS ##
logging.setLoggerClass(BasicLogger)

def getLogger(name):
    return logging.getLogger(name)