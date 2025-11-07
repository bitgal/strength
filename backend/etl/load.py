import json
from backend.config import FOR_MYSQL_DIR
from backend.models.models import Exercise
from backend.models.enum import Equipment
from sqlalchemy.orm import Session

def load_exercises(db_manager):
    """Load exercises from JSON into database"""
    
    exercises_file = FOR_MYSQL_DIR / "exercises.json"
    with open(exercises_file, "r") as f:
        exercises_data = json.load(f)
    
    db = db_manager.sessionLocal()
    
    try:
        for exercise_data in exercises_data:
            # create Exercise object
            exercise = Exercise(
                name=exercise_data.get('name'),
                description=exercise_data.get('description'),
                image_path_1=exercise_data.get('image_path_1'),
                image_path_2=exercise_data.get('image_path_2'),
                equipment=exercise_data.get('equipment')
            )
            db.add(exercise)
        
        db.commit()
        print(f"Loaded {len(exercises_data)} exercises into database")
    except Exception as e:
        db.rollback()
        print(f"Error loading exercises: {e}")
    finally:
        db.close()