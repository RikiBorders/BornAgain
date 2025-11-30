from dataclasses import dataclass
from typing import Optional

@dataclass
class Song:
    title: str
    artist: str
    link: Optional[str]
    filePath: str