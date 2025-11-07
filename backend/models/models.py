
from sqlalchemy import Column, Integer, String, Text, Date, Enum, ForeignKey, Table
from sqlalchemy.orm import relationship, validates
from backend.core.db import Base
from backend.models.enum import Equipment, UserRole
from backend.utils.pwd import hash_password, verify_password

# ===== n:n Join Tables ==============================================================

# n:n
training_plans_exercises = Table(
    'training_plan_exercise', Base.metadata,
    Column('training_plan_id',Integer, ForeignKey('training_plans.id'),primary_key=True),
    Column('exercise_id',Integer, ForeignKey('exercises.id'),primary_key=True),
    extend_existing=True
)

# ===== Models ==============================================================

class BaseRepr:
    def __repr__(self):
        fields = ", ".join(
            f"{col.name}={getattr(self, col.name)!r}"
            for col in self.__table__.columns
        )
        return f"<{self.__class__.__name__}({fields})>"

class Exercise(Base, BaseRepr):
    __tablename__="exercises"
    __table_args__ = {'extend_existing': True}

    id=Column(Integer,primary_key=True, autoincrement=True)
    name=Column(String(200),nullable=False,unique=True)
    description=Column(Text)
    image_path_1=Column(String(255))
    image_path_2=Column(String(255))
    equipment= Column(String(200))
    # equipment= Column(Enum(Equipment),nullable=True)

class TrainingPlan(Base, BaseRepr): # user:trainingPlan 1:n
    __tablename__="training_plans"
    # __table_args__ = {'extend_existing': True}

    id=Column(Integer,primary_key=True, autoincrement=True)
    name=Column(String(100), nullable=False, default="Untitled Training Plan")
    user_id=Column(Integer, ForeignKey("users.id"),nullable=False)
    user = relationship("User",back_populates="training_plans") # training_plans-user n:1

class User(Base,BaseRepr):
    __tablename__="users" 
    # __table_args__ = {'extend_existing': True}
    
    id=Column(Integer,primary_key=True, autoincrement=True)
    username=Column(String(100),nullable=False)
    email=Column(String(100),nullable=False, unique=True)
    password=Column(String(100),nullable=False) # TODO
    training_plans = relationship("TrainingPlan",back_populates="user") # training_plans-user n:1

    @validates('username')
    def validate_username(self, key, value):
        # If username is empty or None, use email as default
        return value or self.email
    
    # validation before inserting to db
    @validates('password')
    def validate_password(self, key, value):
        if not value:
            raise ValueError("Password cannot be empty")
        return value
    
from sqlalchemy.orm import configure_mappers
configure_mappers()
    