from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.db import get_db
from crud.user_repository import UserRepository
from utils.pwd import hash_password



# from utils.pwd import hash_password, verify_password # TODO
from api.schemas import UserBase, UserCreate, UserLogin, UserRead, ExerciseBase, ExerciseRead, ExerciseCreate, TrainingPlanBase, TrainingPlanCreate, TrainingPlanRead
from models.models import User, Exercise, TrainingPlan

users_router = APIRouter(prefix="/users", tags=["users"])
exercises_router = APIRouter(prefix="/exercises", tags=["exercises"])
training_plans_router = APIRouter(prefix="/training_plans", tags=["training_plans"])

###

@users_router.get("/", response_model=list[UserRead])
def list_users(db: Session = Depends(get_db)):
    repo = UserRepository(db)
    return repo.get_users()

@users_router.post("/authenticate", response_model=UserRead)
def authenticate_user(credentials: UserLogin, db: Session = Depends(get_db)):
    print(credentials)
    repo = UserRepository(db)
    u = repo.authenticate(credentials.email, credentials.password)
    print("**************************")
    print(u)
    if not u:
        raise HTTPException(status_code=401, detail="Invalid name or password")
    return u

@users_router.post("/register", response_model=UserRead)
def create_user(user:UserCreate, db:Session=Depends(get_db)):
    repo = UserRepository(db)
    #new_user = User(**user.model_dump())
    hashed_pw = hash_password(user.password)
    new_user = User(email=user.email, password=hashed_pw, username=user.username)
    print("RRRREEEEEGGGGIIIISSSTTTEEERRRRRR")
    print(repr(hashed_pw))  # see exactly what string is stored
    print(repr(user.password))  # see exactly what comes from DB

    return repo.create_user(new_user)

# @user_router.get("/{user_id}", response_model=UserRead)
# def get_user(user_id: int, db: Session = Depends(get_db)):
#     repo = UserRepository(db)
#     user = repo.get_user_by_id(user_id)
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user

# @user_router.get("/{user_id}/training_plans", response_model=list[TrainingPlanRead]) #/users/2/training_plans
# def get_todos_by_user(user_id: int, db: Session = Depends(get_db)):
#     repo = TodoRepository(db)
#     return repo.get_todos_by_user(user_id)


# # ===== Exercises ==============================================================

# @exercise_router.post("/", response_model=TodoRead)#http://127.0.0.1:8000/todos/?user_id=1
# def create_todo(todo: TodoCreate, user_id: int, db: Session = Depends(get_db)):
#     repo = TodoRepository(db)
#     todo_db = Todo(**todo.model_dump(), user_id=user_id)
#     return repo.create_todo(todo_db)
# ##>>
# @todo_router.put("/{todo_id}/state", response_model=TodoRead) #
# def update_todo_state(todo_id: int, new_state: str, db: Session = Depends(get_db)):
#     '''  
#         Example-URL:http://127.0.0.1:8000/todos/1/state?new_state=DONE
#     '''
#     repo = TodoRepository(db)
#     todo = repo.update_todo_state(todo_id, new_state)
#     if not todo:
#         raise HTTPException(status_code=404, detail="Todo not found")
#     return todo

# @todo_router.delete("/{todo_id}", response_model=bool)
# def delete_todo(todo_id: int, db: Session = Depends(get_db)):
#     repo = TodoRepository(db)
#     return repo.delete_todo(todo_id)


# @user_router.post("/authenticate", response_model=UserRead)
# def authenticate_user(credentials: UserLogin, db: Session = Depends(get_db)):
#     repo = UserRepository(db)
#     user = repo.authenticate(credentials.name, credentials.password)
#     if not user:
#         raise HTTPException(status_code=401, detail="Invalid name or password")
#     return user

# # ===== TrainingPlans ==============================================================

# @training_plan_router.post("/", response_model=TrainingPlanRead)#http://127.0.0.1:8000/todos/?user_id=1
# def create_todo(todo: TodoCreate, user_id: int, db: Session = Depends(get_db)):
#     repo = TodoRepository(db)
#     todo_db = Todo(**todo.model_dump(), user_id=user_id)
#     return repo.create_todo(todo_db)
# ##>>
# @training_plan_router.put("/{todo_id}/state", response_model=TodoRead) #
# def update_todo_state(todo_id: int, new_state: str, db: Session = Depends(get_db)):
#     '''  
#         Example-URL:http://127.0.0.1:8000/todos/1/state?new_state=DONE
#     '''
#     repo = TodoRepository(db)
#     todo = repo.update_todo_state(todo_id, new_state)
#     if not todo:
#         raise HTTPException(status_code=404, detail="Todo not found")
#     return todo

# @training_plan_router.delete("/{todo_id}", response_model=bool)
# def delete_todo(todo_id: int, db: Session = Depends(get_db)):
#     repo = TodoRepository(db)
#     return repo.delete_todo(todo_id)


#TODO:
# Add Error Handling: Consider adding error handling to manage potential issues, such as duplicate emails.
# Use create_user instead of repo.create_user: Ensure that the method name is consistent with your repository methods.
# Use model_dump for Data Manipulation: If you need to manipulate the data before creating the user, consider using model_dump to convert the Pydantic model to a dictionary.
# Use await for Asynchronous Operations: If your create_user method is asynchronous, make sure to use await to handle the operation properly.