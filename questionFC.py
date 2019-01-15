#Initialize variables
q1Check = bool(False)
q1Answer = str("")
score = int()
q1 = str("""1. What is the technique called by which the genome of an organism can be
split up into different sized molecules?
    a. Electrolysis
    b. Electrophrosis
    c. Chromatography
    d. None of the above\n""")

#Gives the user information on what the program does, and how to properly use it
print("""This is a one question science quiz. There will be four possible answers,
and only one of them is correct. When selecting answers, enter the letter that
precedes it.\n""")

#Will try to get an acceptable answer from the user while q1Check is False
while q1Check == False:
        #Try to get an input of the specified type....
        try:
                #Gets an input from the user and ensures that it's of type string
                q1Answer = str(input(q1))
                #Sets whatever the user input is to the lowercase version of it
                q1Answer = q1Answer.lower()
                #Checks to see if the input is the correct answer
                if q1Answer == "b":
                        print("Got your answer choice!")
                        #Incerement the scorekeeping variable by 1
                        score  += 1
                        q1Check = True
                #If it isn't check to see if it's an acceptable answer
                elif "`" < q1Answer < "e":
                        print("Got your answer choice!")
                        q1Check = True
                #If it isn't provide feedback
                else:
                        print("""Please enter a letter that is between the
letters A and D.\n""")
        #If it doesn't skip directly here
        except ValueError:
                print("""Please enter a letter. Select your answer choice by putting in
the letter that precedes your answer choice.""")

#Print the user's score in terms of a percentage
print("Your score is:", score*100, "%")
