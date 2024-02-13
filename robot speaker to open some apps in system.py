# dadan nam ekhtesary pt be pyttsx3
import pyttsx3 as pt 
#dastresi be barkhi az amalkardhaye system ba os 
import os 
# yeki az method haye pt ke be komak an system shoro be sohbat mikonad 
pt.speak("hello my friend , i hope your good ")
pt.speak("can you say what is my name ?")
name=input("Enter the robot name ==> ")
pt.speak('thanks. my name is ' + name)
pt.speak("honestly i can open some apps in your system ")
pt.speak("if you ok write ok ")
pt.speak("if dont like to do it , write no")
answear=input("write ok or no ==>")
while  answear == "ok":
    pt.speak("which app dou you like to open ?")
    app_name = input("which app do you want to open ==> ")
    #open vlc media player 
    if app_name == "vlc":
        pt.speak("this  app will be open  soon ")
        os.system('start VLC ')
        pt.speak("app has been opened")
        pt.speak("do you want to continue opening other apps?")
        contine=input("yes or no==>")
        if contine=="no":
            pt.speak("ok , see  you later!")
            break
        else:
            continue
    #open firefox 
    if app_name == "firefox":
        pt.speak("this  app will be open , soon ")
        os.system('start Firefox')
        pt.speak("app has been opened")
        pt.speak("do you want to continue opening other apps?")
        contine=input("yes or no==>")
        if contine=="no":
            pt.speak("ok , see  you later!")
            break
        else:
            continue
     #open chrome  
    if app_name == "chrome":
        pt.speak("this  app will be open ") 
        os.system("start Chrome ")
        pt.speak("app has been opened")
        pt.speak("do you want to continue opening other apps?")
        contine=input("yes or no==>")
        if contine=="no":
            pt.speak("ok , see  you later!")
            break
        else:
            continue
    #open file explorer 
    if app_name == "file explorer":
        pt.speak("this  app will be open , soon ")
        os.system('start Explorer')
        pt.speak("app has been opened")
        pt.speak("do you want to continue opening other apps?")
        contine=input("yes or no==>")
        if contine=="no":
            pt.speak("ok , see  you later!")
            break
        else:
            continue
    # open microsoft edge 
    if app_name == "edge":
        pt.speak("this  app will be open , soon ")
        os.system('start  msedge')
        pt.speak("app has been opened")
        pt.speak("do you want to continue opening other apps?")
        contine=input("yes or no==>")
        if contine=="no":
            pt.speak("ok , see  you later!")
            break
        else:
            continue
    #open visual studio code 
    if app_name == "vs code":
        pt.speak("this  app will be open , soon ")
        os.system('start  Code')
        pt.speak("app has been opened")
        pt.speak("do you want to continue opening other apps?")
        contine=input("yes or no==>")
        if contine=="no":
            pt.speak("ok , see  you later!")
            break
        else:
            continue
    # open calculator 
    if app_name == "calculator":
        pt.speak("this  app will be open , soon ")
        os.system('start  Calc')
        pt.speak("app has been opened")
        pt.speak("do you want to continue opening other apps?")
        contine=input("yes or no==>")
        if contine=="no":
            pt.speak("ok , see  you later!")
            break
        else:
            continue
    # open notepad
    if app_name == "notepad":
        pt.speak("this  app will be open , soon ")
        os.system('start Notepad')
        pt.speak("app has been opened")
        pt.speak("do you want to continue opening other apps?")
        contine=input("yes or no==>")
        if contine=="no":
            pt.speak("ok , see  you later!")
            break
        else:
            continue
    # open cmd 
    if app_name == "cmd":
        pt.speak("this  app will be open , soon ")
        os.system("start cmd")
        pt.speak("app has been opened")
        pt.speak("do you want to continue opening other apps?")
        contine=input("yes or no==>")
        if contine=="no":
            pt.speak("ok , see  you later!")
            break
        else:
            continue
        #
else : 
    if answear == "no":
        pt.speak("sorry for that ")
        pt.speak("do you have another request ? ")
        answear2=input(" enter yes or no ==>")
        if answear2=="yes":
                pt.speak("what can i do for you ")
                #.
                #.
                #.
                #.
                #.
                #.
                #.

        else :
            if answear2=="no":
                pt.speak("ok , goodbye my friend. have a nice time  ")
                exit
          
    