from backend.models.models import TrainingPlan
from sqlalchemy.orm import Session

class TrainingPlanRepository:
    def __init__(self,session:Session):
        self.session=session

    def create_training_plan(self,tp:TrainingPlan)->TrainingPlan:
        self.session.add(tp)
        self.session.commit()
        self.session.refresh(tp)
        return tp

    def get_training_plans_by_user(self, user_id:int) -> list[TrainingPlan]:
        return self.session.query(TrainingPlan).filter(TrainingPlan.user_id == user_id).all()