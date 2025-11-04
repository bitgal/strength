# TODO populate enum value list from actual data seeded
from enum import Enum

class UserRole(Enum):
    TRAINER ="trainer"
    TRAINEE = "trainee"

class ExerAccessory(Enum):
    DUMBBELLS ="Dumbbells"
    BELT = "Belt"

class ExerMachine(Enum):
    SMITH ="Smith Machine"
    FUNCTIONAL = "Functional Trainer"
