from typing import Dict, Any, Union
from rich.console import Console, Text


class BaseExceptionHandler(Exception):
    @staticmethod
    def terminate_program() -> None:
        exit()


class ExMessageHandler(BaseExceptionHandler):
    def __init__(self, message: Text, terminate_after: bool = False):
        self.message = message
        self.__error_message()
        if terminate_after:
            self.terminate_program()

    def __error_message(self):
        Console().print(self.message)