# import sys
# from pathlib import Path
# from backend.config import PROJECT_ROOT
# Add project root to Python path
# sys.path.insert(0, str(PROJECT_ROOT))

from fastapi import FastAPI
from backend.api.routers import users_router, exercises_router, training_plans_router
from backend.core.db import Base, db_manager, get_db
from backend.etl.load import load_exercises
from backend.etl.transform import transform

app = FastAPI()
app.include_router(users_router)
app.include_router(exercises_router)
app.include_router(training_plans_router)

Base.metadata.create_all(bind=db_manager.engine)
# transform()
# load_exercises(db_manager)

if __name__=="__main__":
    import uvicorn
    uvicorn.run("backend.main:app",host="127.0.0.1",port=8000,reload=True)