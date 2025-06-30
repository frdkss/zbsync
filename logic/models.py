from dataclasses import dataclass
from datetime import date
from typing import Any, List


@dataclass
class FileMeta:
    path: str
    tags: List[str]  # ЗУП/БУХ
    date: date
    month: int
    day: int
    quarter: int
    idx: int  # индекс кварталов
    term: int  # индекс сроков
    code: str
    table: List[List[Any]]  # таблица
