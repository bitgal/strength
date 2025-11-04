from fastapi import FastAPI
from api.routers import users_router, exercises_router, training_plans_router
from core.db import Base, db_manager, get_db

app = FastAPI()
app.include_router(users_router)
app.include_router(exercises_router)
app.include_router(training_plans_router)

Base.metadata.create_all(bind=db_manager.engine)

if __name__=="__main__":
    import uvicorn
    uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)