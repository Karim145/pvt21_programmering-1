import requests
import random

response = requests.get("https://bjornkjellgren.se/quiz/v2/questions")
data_list_questions = response.json()
list_id = []
print(len(data_list_questions['questions']))
for i in range(0, len(data_list_questions['questions'])):
    list_id.append(i)
randomlist = random.sample(list_id, k=10)
list_svarade_fel_questions = []
list_av_din_fel_svar = []

def check_correct_input(answer,antal_svar):
    if answer <=0:
        print(f"frågan har {antal_svar} svar, och skall bara siffriorna 1={antal_svar}"),print("----------------"),exit()

def check_corrected_answers (count, antal, correct_answers):
    procent = 100 * float(correct_answers) / float[antal]
    if count < antal and antal != int(i):
        return
    print(f"du fick (str{correct_answers} poäng av (str{antal}) möjliga get fer [str{procent})% rätt")
    print("-----------------------------------------"),exit()


def print_ut_questions_you_answered_wrong(list_svarade_fel_questions,list_of_din_fel_svar):
    global correct_answer_possition2
    print (f"----------------- Check den rätta svaret!!!!!!!!------------------------------")
    print (f"List på rätta och falska svar du matade in ")
    print (f"")
    for n in range(len(list_svarade_fel_questions)):
        print(f"Fråga {data_list_questions['questions'][list_svarade_fel_questions[n]]['id']}. {data_list_questions['questions'][list_svarade_fel_questions[n]]['prompt']} ")
        for q in range (len(data_list_questions['questions'][list_svarade_fel_questions[n]]['answers'])):

            if data_list_questions['questions'][list_svarade_fel_questions[n]]['answers'][q]['correct']:
                correct_answer=data_list_questions['questions'][list_svarade_fel_questions[n]]['answers'][q]['answer']
                correct_answer_possition2=q+1
            print (f"{q+1}. {data_list_questions['questions'][list_svarade_fel_questions[n]]['answers'][q]['answer']}")
        print(f"Ditt svar: {(list_av_din_fel_svar[n])+1}.{data_list_questions['questions'][list_svarade_fel_questions[n]]['answers'][list_av_din_fel_svar[n]]['answer']} vär Fel... Det blir {correct_answer_possition2}.{correct_answer}")
        print("-------------------------------------------------------------")



def game():
    try:
        global antal
        antal=len(randomlist)
        print("----------------------------------------"),print("Svara på 10 slumpmässiga frågor från APIe för att vinna: "),print("--------------------------------")
        count=0
        correct_answers=0
        for i in range(len(randomlist)):
                print(f"Fråga {data_list_questions['questions'][randomlist[i]]['id']}. {data_list_questions['questions'][randomlist[i]]['prompt']} ")
                correct_answer_possition=""
                for q in range (len(data_list_questions['questions'][randomlist[i]]['answers'])):

                    if data_list_questions['questions'][randomlist[i]]['answers'][q]['correct']:
                        correct_answer=data_list_questions['questions'][randomlist[i]]['answers'][q]['answer']
                        correct_answer_possition=q+1
                    print (f"{q+1}. {data_list_questions['questions'][randomlist[i]]['answers'][q]['answer']}")
                antal_svar=(len(data_list_questions['questions'][randomlist[i]]['answers']))
                print(antal_svar)
                answer = input(f"Svara här --> ")
                check_correct_input(int(answer),(antal_svar))
                count += 1
                if int(answer.strip()) == int(correct_answer_possition):
                    print("---------------------------------")
                    correct_answers += 1
                else:
                    list_svarade_fel_questions.append(randomlist[i]), list_svarade_fel_questions.append(int(answer)-1)
                    print("---------------------------------")
                if count>=antal or antal==int(1):
                    if len(list_svarade_fel_questions)>0:
                        print_ut_questions_you_answered_wrong(list_svarade_fel_questions,list_av_din_fel_svar)
                    else:
                        print("Grattis du svarade rätt på alla frågor!!!!")
                    check_corrected_answers(count,antal,correct_answers)
    except ValueError:
        print("Detta är ej ett nummer!:  Du kan bara skriva nummer här ")
        print("------------------------------------"),game()
if __name__ == '__main__':
    game()



