#Quiz game 
print("Welcome to My Pc quiz ❤️❤️")

playing = input("Do you want to play ? ")
if playing.lower() != "yes" :
    quit()
else : 
    print("ok! lets play ==> ")  
score = 0
#question 1
answer_1= input("what does CPU stand for ? ")
if answer_1.lower() == "central proccesing unit" :
    print("Correct👍")
    score += 1
else : 
    print("Incorrect ❌❗")
#question 2
answer_2 = input("what does GPU stand for ? ")
if answer_2.lower() == "graphic proccesing unit" :
    print("Correct👍")
    score += 1 
else : 
    print("Incorrect ❌❗")
#question 3
answer_3 = input("what does RAM stand for ?")
if answer_3.lower() == "random access memory" :
    print("Correct👍")
    score += 1

else : 
    print("Incorrect ❌❗")
#question 4
answer_4 = input("what does PSU stand for ?")
if answer_4.lower() == "power supply" :
    print("Correct👍")
    score += 1
else : 
    print("Incorrect ❌❗")
print("Excellent . you got " + str(score) + " question correct !")

