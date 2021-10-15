import json

with open("que.json") as f:
    questions = json.load(f)

def print_enumerated_answers(answers):
    for ans_num, answer in enumerate(answers, start=1):
        print(f"[{ans_num}] {answer['answer']}")

def main():
   for question in questions['questions']:
       print(question['prompt'])
       answers = question['answers']

       print_enumerated_answers(answers)
       user_answer = int(input(">"))

       if answers[user_answer - 1]['correct']:
           print("Rätt")
       else:
           print("Fel")

if __name__ == '__main__':
    main()
    
