import json

with open('backend/data/for_mysql/exercises.json', 'r') as f:
    exercises = json.load(f)

# Get all unique equipment values
equipment_values = set()

for exercise in exercises:
    equipment = exercise.get('equipment')
    if equipment:
        equipment_values.add(equipment)

equipment_values = sorted(equipment_values)

print(f"Found {len(equipment_values)} unique equipment values:\n")
for value in equipment_values:
    print(f"  - {value}")

# Generate enum code snippet
print("\n\nEnum code snippet for models.py:")
print("class Equipment(Enum):")
for value in equipment_values:
    # Convert to SCREAMING_SNAKE_CASE for enum name
    enum_name = value.upper().replace(" ", "_").replace("-", "_")
    print(f'    {enum_name} = "{value}"')