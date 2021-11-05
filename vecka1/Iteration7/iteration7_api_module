import requests
import random


QUIZ_URL = "https://bjornkjellgren.se/quiz/v2/questions"
response = requests.get(QUIZ_URL)

try:
    response.raise_for_status()
except requests.HTTPError as e:
    print("Connection error"),exit()
response =response.json()

randomlist=random.sample(list(filter(lambda x : int(x['id']), response['questions'])), k=10)


def post_svaret(question_nr, ditt_svar):
    r=requests.get(QUIZ_URL).json()
    payload = {"id":question_nr ,"Rätt":ditt_svar}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r= requests.post(QUIZ_URL, json=payload, headers=headers)
