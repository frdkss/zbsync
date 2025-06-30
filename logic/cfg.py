from typing import Dict, List

TEMPLATE: str = "template.xlsx"
OUTPUT: str = "output.xlsx"

ZUP_KEYS: List[str] = ["зуп"]
BUH_KEYS: List[str] = ["бух"]
ZUP_TEXT: str = "Ведомость в кассу"
BUH_TEXT: str = "Выдача наличных"

MONTHS: Dict[int, str] = {
    1: "январь", 2: "февраль", 3: "март",
    4: "апрель", 5: "май", 6: "июнь",
    7: "июль", 8: "август", 9: "сентябрь",
    10: "октябрь", 11: "ноябрь", 12: "декабрь",
}

CODES: Dict[int, Dict[int, str]] = {
    1: {1: "021", 2: "022"},
    2: {1: "023", 2: "024"},
    3: {1: "025", 2: "026"},
}
