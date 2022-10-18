
import unittest
from types import *

class variabel_sträng("self"):
    def __init__(self) -> None:
        super().__init__()

class variabel_heltal("self"):
    def __init__(self) -> None:
        super().__init__()

class variabel_flyttal("self"):
    def __init__(self) -> None:
        super().__init__()

class variabel_boolean("self"):
    def __init__(self) -> None:
        super().__init__()

assert variabel_sträng == "Hej"
assert type(variabel_sträng) == str

assert variabel_heltal == 3
assert type(variabel_heltal) == int

assert variabel_flyttal == 0.5
assert type(variabel_flyttal) == float

assert variabel_boolean == True
assert type(variabel_boolean) == bool


