import sys
from networksecurity.logging import logger
class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        _, _, exc_tb = error_detail.exc_info()
        self.line_no = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename
        self.error_message = str(error_message)

    def __str__(self):
        return 'Error occurred in python script [{0}] line number [{1}] error message [{2}]'.format(
            self.file_name, self.line_no, self.error_message
        )


