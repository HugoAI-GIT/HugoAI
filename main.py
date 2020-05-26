#ALL IMPORTS
import http.server
import socketserver
import time
import sys
#Variables
PORT = 10180
Handler = http.server.SimpleHTTPRequestHandler

LAN = ""

question_prompts_EN = "What is your language ? [FR/EN]"
question_prompts_FR = "Voulez-vous de l'aide grace à la plateforme web ?"

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

if LAN == "FR":
    answer = input("Voulez-vous avoir la page d'aide en ligne ? [O/N]")
    if answer == "O":
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print("Serveur ouvert ! Sur le port : ", PORT)
            #httpd.serve_forever()
