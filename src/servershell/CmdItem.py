from dataclasses import dataclass
from datetime import datetime


@dataclass
class CmdItem:
    """Class to represent a command item to be listed in the index.html"""
    name: str
    path: str = ""
    date: datetime = datetime.now()
