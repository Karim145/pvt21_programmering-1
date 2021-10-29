import requests
import random

response = requests.get("https://bjornkjellgren.se/quiz/v1/questions")
data_List_questions = response.json() # hämtar all data i jason format

lis_id=[]
for i in range(0,len(data_List_questions['questions'])):
    lis_id.append(i)  #Skapa en lista med numren på alla frågor
randomlist = random.sample(lis_id, k=10) #gör en random lista med 10 sifrror från listan övan på 
list_svarade_fel_questions=[]
list_of_din_fel_svar=[]
def check_correct_input(answer,antal_svar):
    if answer>antal_svar or answer<=0:
        print(f"Frågan har {antal_svar} svar, och skall bara siffrorna 1-{antal_svar} accepteras som input. Försök igen "), print("----------------"),game()

def check_corrected_answers(count,antal,correct_answers):
    percentage = 100 * float(correct_answers)/float(antal) # räknara procent på rätta svar 
    if count>=antal or antal==int(1):
        print(f"Du fick {str(correct_answers)} poäng av {str(antal)} möjliga.Det ger {str(percentage)}% rätt" )
        print("------------------------------------------"),exit()

def print_ut_questions_you_answered_wrong(list_svarade_fel_questions,list_of_din_fel_svar):
    print (f"----------------- Kontrollera korrekta svaret!------------------------------")
    print (f"-----------------lista på både rätta och falska frågor----------------------")
    print (f"")
    for n in range(len(list_svarade_fel_questions)):
        print(f"Fråga {data_List_questions['questions'][list_svarade_fel_questions[n]]['id']}. {data_List_questions['questions'][list_svarade_fel_questions[n]]['prompt']} ")
        for q in range (len(data_List_questions['questions'][list_svarade_fel_questions[n]]['answers'])):
            #tar rätta svaret från json filen
            if data_List_questions['questions'][list_svarade_fel_questions[n]]['answers'][q]['correct']:
                correct_answer=data_List_questions['questions'][list_svarade_fel_questions[n]]['answers'][q]['answer']
                correct_answer_possition2=q+1
            print (f"{q+1}. {data_List_questions['questions'][list_svarade_fel_questions[n]]['answers'][q]['answer']}")
        print(f"Ditt svar: {(list_of_din_fel_svar[n])+1}.{data_List_questions['questions'][list_svarade_fel_questions[n]]['answers'][list_of_din_fel_svar[n]]['answer']} var Fel... Det blir {correct_answer_possition2}.{correct_answer}")
        print("-------------------------------------------------------------")

def game():
    try: 
        global antal
        antal=len(randomlist)
        print("----------------------------------------"),print("Du kommer att få svara på 10 slumpmässiga frågor"),print("--------------------------------")
        count=0
        correct_answers=0
        for i in range(len(randomlist)):
            print(f"Fråga {data_List_questions['questions'][randomlist[i]]['id']}. {data_List_questions['questions'][randomlist[i]]['prompt']} ")
            correct_answer_possition=""
            for q in range (len(data_List_questions['questions'][randomlist[i]]['answers'])):
                #take the correct answer from the json object
                if data_List_questions['questions'][randomlist[i]]['answers'][q]['correct']:
                    correct_answer=data_List_questions['questions'][randomlist[i]]['answers'][q]['answer']
                    correct_answer_possition=q+1
                print (f"{q+1}. {data_List_questions['questions'][randomlist[i]]['answers'][q]['answer']}")
            antal_svar=(len(data_List_questions['questions'][randomlist[i]]['answers']))
            answer = input(f"Answer here --> ")
            check_correct_input(int(answer),int(antal_svar))
            count += 1
            if int(answer.strip()) == int(correct_answer_possition): 
                print("---------------------------------")
                correct_answers += 1
            else:
                list_svarade_fel_questions.append(randomlist[i]), list_of_din_fel_svar.append(int(answer)-1)
                print("---------------------------------")
            if count>=antal or antal==int(1):
                if len(list_svarade_fel_questions)>0:
                    print_ut_questions_you_answered_wrong(list_svarade_fel_questions,list_of_din_fel_svar) #skriver ut de frågor man svarade på
                else:
                    print("Grattis du svarade rätt på alla frågor!!!!")
                check_corrected_answers(count,antal,correct_answers) #anropa en funktion för att beräkna korrekta svar
    except ValueError:
        print("Detta är ej ett nummer!: Försök igen ")
        print("------------------------------------"),game()
if __name__ == '__main__':
    game()

