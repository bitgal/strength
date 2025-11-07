from backend.models.models import Exercise
from sqlalchemy.orm import Session

class ExerciseRepository:
    def __init__(self,session:Session):
        self.session=session

    def get_exercises(self) -> list[Exercise]:
        return self.session.query(Exercise).all()