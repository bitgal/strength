import json
import os
from backend.config import PROCESSED_DATA_DIR, FOR_MYSQL_DIR
# from backend.models.enum import Equipment

def transform():

    processed_exercises_file = PROCESSED_DATA_DIR / "exercises.json"
    with open(processed_exercises_file, "r") as f:
        exercises = json.load(f)

    transformed = []

    for exercise in exercises:
        images = exercise.get("images", [])

        image_path_1 = images[0] if len(images) > 0 else None
        image_path_2 = images[1] if len(images) > 1 else None

        equipment_str = exercise.get("equipment").strip()
        if equipment_str is None or equipment_str.lower() in ("body only", ""):
            equipment = "no equipment"
        elif equipment_str.lower() == "other":
            equipment = "other accessory"
        else:
            equipment = equipment_str

        if isinstance(exercise.get("instructions"), list):
            description = "\n".join(exercise.get("instructions", [])) 
        else:
            description = exercise.get("instructions", "")

        record = {
            "name": exercise.get("name", "n/a"),
            "description": description,
            "image_path_1": image_path_1,
            "image_path_2": image_path_2,
            "equipment": equipment
        }

        transformed.append(record)

    os.makedirs(FOR_MYSQL_DIR, exist_ok=True)
    mysql_ready_exercises_file = FOR_MYSQL_DIR / "exercises.json"
    with open(mysql_ready_exercises_file, "w") as f:
        json.dump(transformed, f, indent=2)

    print(f"Transformed {len(transformed)} exercises")
    print(f"Saved to data/for_mysql/exercises.json")

    # preview first record
    if transformed:
        print("\nFirst record preview:")
        print(json.dumps(transformed[0], indent=2))