from models.models import User, Exercise, TrainingPlan
from sqlalchemy.orm import Session
from utils.pwd import verify_password

class UserRepository:
    def __init__(self,session:Session):
        self.session=session

    def create_user(self,user:User)->User:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def authenticate(self, email: str, password: str) -> User | None:
            user = self.session.query(User).filter(User.email == email).first()
            print("AAAAUUUUTHENTICATEEEEEE")
            print(user)
            if user and verify_password(password, user.password):
                return user
            return None
    
    def get_users(self) -> list[User]:
        return self.session.query(User).all()