
class Answer:
    answer: str
    correct: bool

    def __init__(self, answer, correct):
        self.answer = answer
        self.correct = correct

def __str__(self):
    return self.answer

def parse_answers(answers) :
    res = []
    for a in answers:
        res.append((a['answer'], a['correct']))
    return res


class Question(Answer): #Den här klassen bearbetar frågorna och beräknar procentandelen av korrekta svar

    id: int
    prompt: str
    times_asked: int
    times_correct: int

def __init__(self, id_, prompt, times_asked, times_correct):
    self.id = int(id_)
    self.prompt = prompt
    self.times_asked = int(times_asked)
    self.times_correct = int(times_correct)

def parse_question(q) :
    return q['id'], q['prompt'], q['times_asked'], q['times_correct'], parse_answers(q['answers'])

def percent_correct(self) -> str:
    toreturn= (int(self[0])/ int(self[1]))
    return f"{toreturn:.0%}"


class Statistik(Question,Answer):

    def __init__(self, answer, correct):
        super().__init__(answer, correct)

def check_correct_input(your_answer,antal_svar):
    if your_answer>antal_svar or your_answer<=0:
        print("-" * 80)
        print(f" **** Du kommer att få svara på frågorna på nytt!! ****")
        print(f"Frågan har {antal_svar} svar, och endast siffror 1-{antal_svar} accepteras som input. Försök igen med bokstaver "),main()

def get_questions():
    res = []
    for q in randomlist:

        res.append(parse_question(q))
    return res

def main():

    try:

        antal=len(randomlist)
        print("-" * 80),print("Du kommer att få svara på 10 slumpmässiga frågor från API:ET: "),print("-" * 80)
        correct_svar=0
        list_of_svarade_fel_question=[]
        control_svar=0
        for question in get_questions():
            times_correct=question[3]
            times_asked=question[2]
            print(f'Fråga {question[0]}. [{percent_correct((times_correct,times_asked))} har svarat rätt]. {question[1]}')
            global i, msg
            for i, answer in enumerate((question[4]), start=1):
                answer1=answer[1]
                answer=answer[0]
                print(f"[{i}] {answer}")
                if answer1:
                    control_svar=int(i)
                    msg= f"rätt svar är {i}. {answer}"
            antal_svar=i
            your_answer = int(input(f"Svara här --> "))
            check_correct_input(int(your_answer),int(antal_svar))
            print(f'Ditt svar. {your_answer}')
            if int(control_svar)==int(your_answer):
                correct_answer = f"Rätt!!"
                correct_svar+=1
                ditt_svar=True
            else:
                correct_answer = f'Fel,{msg}'
                list_of_svarade_fel_question.append(f'{question[0]}. {question[1]}')
                list_of_svarade_fel_question.append(f' -> {msg}')
                ditt_svar=False
            print(correct_answer)

            post_svaret(question[0], ditt_svar)
            print("-" * 80)


        print(f'*** RESULTAT ***')
        print(f'Du fick {correct_svar} av {antal} möjliga poäng.')
        if len(list_of_svarade_fel_question) > 0:
            print(f'Du svarade fel på dessa frågor:')
            print(*list(list_of_svarade_fel_question), sep = '\n' )

    except ValueError:
        print("-" * 80)
        print("Det var ingen siffra!  Var vänlig och försök igen! "),main()

if __name__ == '__main__':
    main()
