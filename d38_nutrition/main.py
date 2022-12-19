# import response
import requests
import datetime as dt


APP_ID = "b14e993e"
API_KEY = "3f178a94e892c1028bc82b7ed5bf304a"
headers = {"x-app-id": APP_ID, "x-app-key": API_KEY}
nutrients_endpoint = "https://trackapi.nutritionix.com/v2/natural/nutrients"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

user_exercises = input("Tell me which exercises you did: ")

exercises_params = {
    "query": user_exercises,
    "gender": "male",
    "weight_kg":88,
    "height_cm":178,
    "age": 43}

response = requests.post(url=exercise_endpoint, json=exercises_params, headers=headers)
print(response.text)
data = response.json()["exercises"]
print(data)

date = dt.datetime.today()
ex_date = date.strftime("%d/%m/%Y")
ex_time = date.strftime("%X")

sheety_add_row = "https://api.sheety.co/e29d037c300ced0c7a148893626b3b80/mo1DerWorkout/workouts"

headers2 = {
    "Authorization": "Basic YjE0ZTk5M2U6M2YxNzhhOTRlODkyYzEwMjhiYzgyYjdlZDViZjMwNGE="
}
for activity in range(len(data)):
    exercise_name = (data[activity]["name"]).capitalize()
    print(exercise_name)
    exercise_duration = int((data[activity]["duration_min"]))
    print(exercise_duration)
    exercise_calories = int((data[activity]["nf_calories"]))
    print(exercise_calories)
    activity_params = {
        "workout": {
            "date": ex_date,
            "time": ex_time,
            "exercise": exercise_name,
            "duration": exercise_duration,
            "calories": exercise_calories}}
    push = requests.post(url=sheety_add_row, json=activity_params, headers=headers2)
    print(push.text)

# https://api.sheety.co/username/mo1der_workout/1S5Nc5Vs2eDibRufJJxasSFsVBlrcWapsG3dt2aotBBs


#
# sheety_retrieve_rows = "https://api.sheety.co/e29d037c300ced0c7a148893626b3b80/mo1DerWorkout/workouts"


