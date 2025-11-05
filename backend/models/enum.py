
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

class Equipment(Enum):
    BANDS = "bands"
    BARBELL = "barbell"
    CABLE = "cable"
    DUMBBELL = "dumbbell"
    E_Z_CURL_BAR = "e-z curl bar"
    EXERCISE_BALL = "exercise ball"
    FOAM_ROLL = "foam roll"
    KETTLEBELLS = "kettlebells"
    MACHINE = "machine"
    MEDICINE_BALL = "medicine ball"
    OTHER_ACCESSORY = "other accessory"
