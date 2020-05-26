#ALL IMPORTS
import http.server
import socketserver
import time
import sys
import os
#Variables

LAN = ""

question_prompts_EN = "What is your language ? [FR/EN]"

#class

class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

#Def

def run_quiz():
    answer = input(question_prompts_EN + " ")
    if answer == "FR":
        print("Langue définie sur FR !");
        LAN = "FR"
        # DEBUG
        #print(LAN)
        #time.sleep(3)
        if input("Voulez-vous avoir la page d'aide en ligne ? [O/N]") == "O":
            os.startfile("help.py")
    else:
        if answer == "":
            print("Langue définie sur FR ( Par Défaut ) !");
            LAN = "FR"
        else:
            if answer == "EN":
                print("Language can not set to EN not available")
                time.sleep(2)
                sys.exit()

#CODE

run_quiz()
