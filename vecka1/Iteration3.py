import json
import pprint

with open("que.json") as f:
    questions = json.load(f)

pprint.pprint(questions)

print("#" * 80)

pprint.pprint(questions['questions'][0]['prompt'])
i = 1
for ans in questions['questions'][0]['answers']:
    print(f"[{i}] {ans['answer']}")
    i += 1
guess = input("Ditt svar: ")

if guess == questions['questions'][0]['answers'][0]:
    print(f"Rätt!!!" )
else:
    print(f"Fel, rätt svar är {questions['questions'][0]['answers'][0]}")

