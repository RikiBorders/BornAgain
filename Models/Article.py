from dataclasses import dataclass
from typing import Optional

@dataclass
class Article:
    title: Optional[str]
    body: Optional[str]
    authors: Optional[str]
    image: Optional[str]
    deck: Optional[str]