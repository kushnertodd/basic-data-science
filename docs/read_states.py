import requests

url = "https://gist.githubusercontent.com/kushnertodd/4001ed7df2be5d09c95e7df11a4afcf7/raw/0b4fab8d35dbc1d1f380959f12eb43f25d2674b4/states.csv"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.text
    print(data)
