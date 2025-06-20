from enum import Enum, auto
from abc import ABC, abstractmethod
from datetime import datetime
import sqlite3
import threading
import time


class LogLevel(Enum):
    DEBUG = auto()
    INFO = auto()
    WARNING = auto()
    ERROR = auto()
    FATAL = auto()


class LogMessage:
    def __init__(self, level: LogLevel, message: str):
        self.timestamp = datetime.now()
        self.level = level
        self.message = message

    def format(self):
        return f"{self.timestamp} [{self.level.name}] {self.message}"


class LogAppender(ABC):
    @abstractmethod
    def append(self, message: LogMessage):
        pass


class ConsoleAppender(LogAppender):
    def append(self, message: LogMessage):
        print(message.format())


class FileAppender(LogAppender):
    def __init__(self, file_path="log.txt"):
        self.file_path = file_path

    def append(self, message: LogMessage):
        with open(self.file_path, "a") as f:
            f.write(message.format() + "\n")


class LoggerConfig:  # Strategy Pattern
    def __init__(self, level: LogLevel, appender: LogAppender):
        self.level = level
        self.appender = appender


class Logger:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self.config = None
        self._initialized = True

    def set_config(self, config: LoggerConfig):
        self.config = config

    def log(self, level: LogLevel, message: str):
        if not self.config or level.value < self.config.level.value:
            return
        log_message = LogMessage(level, message)
        self.config.appender.append(log_message)

    def debug(self, msg):
        self.log(LogLevel.DEBUG, msg)

    def info(self, msg):
        self.log(LogLevel.INFO, msg)

    def warning(self, msg):
        self.log(LogLevel.WARNING, msg)

    def error(self, msg):
        self.log(LogLevel.ERROR, msg)

    def fatal(self, msg):
        self.log(LogLevel.FATAL, msg)


class LoggingExample:
    def run(self):
        logger = Logger()
        logger.set_config(LoggerConfig(LogLevel.INFO, ConsoleAppender()))

        logger.info("App started")
        logger.debug("This won't appear - level too low")

        logger.set_config(LoggerConfig(LogLevel.DEBUG, FileAppender("app_log.txt")))
        logger.debug("Now debug will appear in file")

        # Switch to DB appender
        logger.set_config(LoggerConfig(LogLevel.WARNING, ConsoleAppender()))
        logger.warning("Warning stored in DB")
        logger.error("Error stored in DB")

        # Log from multiple threads
        def log_from_thread(thread_id):
            for i in range(3):
                logger.info(f"[Thread {thread_id}] Logging message {i}")
                time.sleep(0.1)

        threads = [
            threading.Thread(target=log_from_thread, args=(i,)) for i in range(2)
        ]
        for t in threads:
            t.start()
        for t in threads:
            t.join()


# Run the example
if __name__ == "__main__":
    LoggingExample().run()
