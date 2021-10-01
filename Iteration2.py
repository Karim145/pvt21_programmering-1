def tf_quiz(question, correct_ans):
    if input(question) == correct_ans:
        return ("Rätt")
    else:
        return ("Fel")

num_correct = 0

questions = [{"question": "Vilken funktion använder vi för att skriva ut saker i terminalen",
              "answer": "print"},
             {"question": "Vilket tecken använder vi för att skriva en kommentar i python",
              "answer": "#"},
             {"question": "När slutar lektionen", "answer": "17:00"}]

for question in questions:
    print(question["question"])
    ans = input(">")
    if ans == question["answer"]:
        print("Rätt")
        num_correct += 1
    else:
        print(f"Fel, rätt svar är {question['answer']}")

print(f"Du fick {num_correct} Rätt")