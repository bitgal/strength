import json
import os
from backend.config import PROCESSED_DATA_DIR, FOR_MYSQL_DIR

processed_exercises_file = f"{PROCESSED_DATA_DIR}/exercises.json"
with open(processed_exercises_file, "r") as f:
    exercises = json.load(f)

transformed = []

for exercise in exercises:
    images = exercise.get("images", [])

    image_path_1 = images[0] if len(images) > 0 else None
    image_path_2 = images[1] if len(images) > 1 else None

    equipment = exercise.get("equipment")
    if equipment in ("body only", None):
        equipment = None
    elif equipment == "other":
        equipment = "other accessory"


    record = {
        "name": exercise.get("name", "n/a"),
        "description": exercise.get("instructions", []),
        "image_path_1": image_path_1,
        "image_path_2": image_path_2,
        "equipment": equipment
    }

    transformed.append(record)

os.makedirs(FOR_MYSQL_DIR, exist_ok=True)
with open(f"{FOR_MYSQL_DIR}/exercises.json", "w") as f:
    json.dump(transformed, f, indent=2)

print(f"Transformed {len(transformed)} exercises")
print(f"Saved to data/for_mysql/exercises.json")

# preview first record
if transformed:
    print("\nFirst record preview:")
    print(json.dumps(transformed[0], indent=2))