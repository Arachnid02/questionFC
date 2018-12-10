q1Check = bool(False)
q1Answer = str("")
q1 = str("""1. What is the technique called by which the genome of an organism can be
split up into different sized molecules?
    a. Electrolysis
    b. Electrophrosis
    c. Chromatography
    d. None of the above\n""")

print("""This is a one question science quiz. There will be four possible answers,
and only one of them is correct. When selecting answers, enter the letter that
precedes it.\n""")

while q1Check == False:
        q1Answer = str(input(q1))
        q1Answer = q1Answer.lower() 
        if "`" < q1Answer < "e":
            if q1Answer == "b":
                print("""Your answer is correct! Electrophrosis is the technique by
which the genome of an organism can be split up into different sized molecules.\n""")
            else:
                print("""Sorry, your answer isn't correct. If you would like to try
again, please restart the quiz.""")
            q1Check = True
        else:
            print("""Please enter your answer choice by putting in the letter
that precedes it.\n""")

