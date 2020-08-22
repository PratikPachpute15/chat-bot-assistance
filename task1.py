import os
import pyttsx3 as t

print("Hey!!! Welcome to Chat Bot Assistance")
t.speak("Hey!!!!!!! Welcome to Chat Bot Assistance")



def menu():
    print("***************\t Service Menu \t****************")
    print("\t 1. Open Google Chorme")
    print("\t 2.Open Notepad")
    print("\t 3.Open Groove Music Player")
    print("\t 4.Open Control Panel")
    print("\t 5.Open MS Word")
    print("\t 6.Open MS Excel")
    print("\t 7.Open Power Point")
    print("\t 8.Open Settings")
    print("\t 9. Open Youtube")
    print("\t 10.Open Facebook")
     

    print("\n++++++++++++++++ Hello! How can I help you? +++++++++++++++ ")
    t.speak("Hello! How can I help you?")
menu()

while True:
    
    print("\n What do you want to open: ",end="")
    t.speak("What do you want to open")
    p=input()
     
#1
    if(("run" in p) or ("open" in p) or ("execute"in p) or ("launch" in p)) and (("chrome" in p) or ("google chrome" in p)):
        print("Launching Google Chrome")
        t.speak("Launching Google Chrome")
        os.system("start chrome")
#2
    elif((("run" in p) or ("open" in p) or ("execute"in p) or ("launch" in p)) and ("notepad" in p)):
        print("Launching Notepad")
        t.speak("Launching Notepad")
        os.system("start notepad")
#3
     
    elif((("run" in p) or ("open" in p) or ("execute"in p) or ("launch" in p))and('groove' in p) ):
        print("Launching Groove Music")
        t.speak("Launching Groove Music")
        os.system("start mswindowsmusic:")
#4
    elif((("run" in p) or ("open" in p) or ("execute"in p) or ("launch" in p)) and ("control panel" in p)):
        print("Launching Control Panel")
        t.speak("Launching Control Panel")
        os.system("control panel")
#5  
    elif((("run" in p) or ("open" in p) or ("execute"in p) or ("launch" in p))and (('word' in p) or ('doc' in p))):
        print("Launching MS Word")
        t.speak("Launching MS Word")
        os.system("winword")
#6   
    elif((("run" in p) or ("open" in p) or ("execute"in p) or ("launch" in p))and(('excel' in p) or ('sheet' in p))) :
        print("Launching MS Excel")
        t.speak("Launching MS Excel")
        os.system("excel")
        
#7 
    elif((("run" in p) or ("open" in p) or ("execute"in p) or ("launch" in p)) and (('ppt' in p) or ('presentation' in p) or ('powerpoint' in p))):
        print("Launching MS Powerpoint Presentation")
        t.speak("Launching MS Powerpoint Presentation")
        os.system("POWERPNT")
#8
    elif((("run" in p) or ("open" in p) or ("execute"in p) or ("launch" in p))and (("setting" in p))):
        print("Launching setting")
        t.speak("Launching setting")
        os.system("start ms-settings:")
#9
    elif((("run" in p) or ("open" in p) or ("execute"in p) or ("launch" in p))and (("youtube" in p) )):
        print("Launching Youtube")
        t.speak("Launching Youtube")
        os.system("start https://www.youtube.com/watch?v=fUeyAItugv8")
#10
    elif((("run" in p) or ("open" in p) or ("execute"in p) or ("launch" in p))and (("facebook" in p)or ("fb" in p) or ("Facebook")or ("Fb"))):
        print("Launching Facebook")
        t.speak("Launching Facebook")
        os.system("start  http://www.facebook.com/")
 

        
    elif ("exit" in p) or ("quit" in p) or ("close" in p):
        print("Thank you for using Chat Bot Assistance....!!Have a nice Day")
        t.speak("Thank you for using Chat Bot Assistance....!!Have a nice Day")
        break  

    else :
        print("Not Found on this PC")
        t.speak("Not Found on this PC")
        #Ask for Searching
        print("May I search on Web  ",end = " ")
        t.speak("May I search on Web  ")
        ans = input().lower()
        #Search on Web
        if((('search' in ans) or ('ok' in ans) or ('can'in ans) or ('yes' in ans) or ('yeah' in ans) or ('yup' in ans) or ('okay' in ans) or ('ohk' in ans)) and not (("don't" in ans) or ("not" in ans) or ("no" in ans) or ("never" in ans))):
            search = "Chrome https://www.google.com/search?q=\""+p+"\""
            os.system(search)
            print("Launching Chrome")
            t.speak("Launching Chrome")
        #Save the Query in Text file named "rawdata.txt"    
        else :
            f=open("rawdata.txt", "a+")
            p =" \n"+p
            f.write(p) 
            f.close() 
            print('Ok')
            t.speak('Ok')



