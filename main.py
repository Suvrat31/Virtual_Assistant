from intro import  intro
from functionality import functionality
from analysis import *
from speech_recog import speech_recog
from training import *
if __name__ == "__main__":
    intro()
    otpion1=input("Do you want to see the current functionality? Yes or No ")
    if(otpion1.lower()=="yes"):
        functionality()
    while(1):
        while(1):
            print()
            print("1 for Voice Input")
            print("2 for Text Input")
            print("3 to create own functionality")
            option=input("Enter Option: ")
            if(option=="1"):
                command=speech_recog().lower()
                break
            elif(option=="3"):
            	usr_fun()
            	break
            else:
                command=input("What do you want to do? ")
                break

        command,command_sentence=run_classifier(command)
        analysis(command,command_sentence)
        temp_var_1=input("Do you want to continue? yes or no").lower()
        if(temp_var_1=="no"):
            break

