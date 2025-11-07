import requests
import json
import os
from backend.config import RAW_DATA_DIR, PROCESSED_DATA_DIR, IMAGES_DIR


BASE_URL = "https://raw.githubusercontent.com/yuhonas/free-exercise-db/main/dist/exercises.json"
IMAGE_PREFIX_URL = "https://raw.githubusercontent.com/yuhonas/free-exercise-db/main/exercises/"

response = requests.get(BASE_URL).json()

os.makedirs(RAW_DATA_DIR, exist_ok=True)
os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)
os.makedirs(IMAGES_DIR, exist_ok=True)

raw_exercises_file = RAW_DATA_DIR / "exercises.json"
with open(raw_exercises_file, 'w') as f:
    json.dump(response, f, indent=2)

#images in json are a relative path
#we get the full path and save them locally:
for exercise in response:
    exercise_images = exercise.get("images", [])  #'images': ['3_4_Sit-Up/0.jpg', '3_4_Sit-Up/1.jpg'],
    new_images = []

    for image_path in exercise_images:
        image_full_url = IMAGE_PREFIX_URL + image_path
        local_path = f"{IMAGES_DIR}/{image_path}"

        # skip if already exists
        if os.path.exists(local_path):
            new_images.append(local_path)
            continue

        img_response = requests.get(image_full_url)

        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        with open(local_path, "wb") as f:
            f.write(img_response.content)

        new_images.append(local_path)

    exercise['images'] = new_images

#save json with local image paths to processed/
processed_exercises_file = PROCESSED_DATA_DIR / "exercises.json"
with open(processed_exercises_file, "w") as f:
    json.dump(response, f, indent=2)

