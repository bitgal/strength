# Training Plan Builder

## Data Source
Exercise data taken from: https://github.com/yuhonas/free-exercise-db/blob/main/README.md

## Database tables

**muss**
users (username, email, password, role)
exercises (name, )
training_plans

exercises-training_plans (n:n)
user-training_plans (1:n)

**kann**
muscles
trainers

## API Docs

### Endpoints
user create (aka register)
user update
user delete
get_user_by_id
get_user_by_email

trainingPlan create
trainingPlan update
trainingPlan delete
get_training_plans_by_user (user_id?)
start_training_plan (?)
end_training_plan (?)

get_all_exercises
filter_exercises (by accessory, machine, primaryMuscle)

## start the app

### using Docker

docker-compose up -d --build

## View the app
 - Streamlit frontend: http://localhost:8502
 - FastAPI backend: http://localhost:8000/docs (interactive API docs)
 - Database: Connect in DBeaver with localhost:3306 (root/root)




