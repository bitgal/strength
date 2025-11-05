from pydantic import BaseModel,Field,ConfigDict
from datetime import date
from backend.models.enum import UserRole, Equipment

# ===== Exercises ==============================================================

class ExerciseBase(BaseModel):
    name: str

# what client will send the endpoint
class ExerciseCreate(ExerciseBase):
    description: str | None = None
    image_path_1: str | None = None
    image_path_2: str | None = None
    equipment: Equipment | None = None

# what the response sent to the client looks like
class ExerciseRead(ExerciseBase):
    id: int
    description: str | None = None
    image_path_1: str | None = None
    image_path_2: str | None = None
    equipment: Equipment | None = None
    # adding Model-config so FastAPI automatically:
    # 1. Converts model to dict (using from_attributes=True)
    # 2. Converts dict to JSON
    # 3. Sends JSON to client
    model_config = ConfigDict(from_attributes=True)

# ===== Training Plans ==============================================================

class TrainingPlanBase(BaseModel):
    name: str

# what client will send the endpoint
class TrainingPlanCreate(TrainingPlanBase):
    pass

# what the response sent to the client looks like
class TrainingPlanRead(TrainingPlanBase):
    id: int
    exercises: list[ExerciseRead]
    # adding Model-config so FastAPI automatically:
    # 1. Converts model to dict (using from_attributes=True)
    # 2. Converts dict to JSON
    # 3. Sends JSON to client
    model_config = ConfigDict(from_attributes=True)



# ===== Users ==============================================================

class UserBase(BaseModel):
    email: str

# validation of request data at endpoint level. returns 422 if invalid
# more validation lives on model level
class UserCreate(UserBase):
    username: str
    password: str = Field(min_length=8, max_length=100)

class UserRead(UserBase):
    id: int
    username: str
    training_plans: list[TrainingPlanRead] = []
    model_config = ConfigDict(from_attributes=True)

# what client needs to send in order to login
class UserLogin(UserBase):
    password: str

