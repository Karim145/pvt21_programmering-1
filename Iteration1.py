def tf_quiz(question, correct_ans):
    if input(question) == correct_ans:
        return("Rätt")
    else:
        return("Fel")

quiz_eval = tf_quiz("Vilken av dessa tecken används för att kommentera koden i python (#/%)", "#")


print("Ditt svar är", quiz_eval)

def tf_quiz(question, correct_ans):
    if input(question) == correct_ans:
        return("Rätt")
    else:
        return("Fel")

quiz_eval = tf_quiz("Vad är rätt filformat för Python-filer (.py, .pyth, .pyt)", ".py")


print("Ditt svar är", quiz_eval)


