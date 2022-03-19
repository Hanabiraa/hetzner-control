from rich.console import Console, Text


class BaseExceptionHandler(Exception):
    """
    Basic abstract class for custom exception
    """

    @staticmethod
    def terminate_program() -> None:
        """
        fast terminate.
        Purpose - for hide traceback
        """
        exit()


class ExMessageHandler(BaseExceptionHandler):
    """
    Exception class, which print in console rich.console.Text object
    """

    def __init__(self, message: Text, terminate_after: bool = False):
        self.message = message
        self.__error_message()
        if terminate_after:
            self.terminate_program()

    def __error_message(self):
        Console().print(self.message)
