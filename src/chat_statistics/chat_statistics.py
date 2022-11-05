import json
from typing import Union
from pathlib import Path


class ChatStatistics:
    def __init__(self, file_path: Union[str, Path]) -> None:
        """read a text file(.json or .txt)

        :param file_path: path to the file
        :type file_path: Union[str, Path]
        """
        with open(file_path) as f:
            self.data = json.load(f)