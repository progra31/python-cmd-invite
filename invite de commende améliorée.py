import random
import os
import time

version="3.5.46"

# init
print("cmd executor")
start_mode=input("press enter to continue or enter a special start imput : ")
if start_mode=="enable.premium":
    print("quick staring enabled")
    time.sleep(1)
    os.system("cls" if os.name == "nt" else "clear")
else:
    print("checking files")
    time.sleep(3)
    print("you are on free/laggy edition")
    print("loading some stuff")
    time.sleep(2)
    print("loading version informations")
    print("loading help cmd")
    time.sleep(2)
    print("almost there")
    time.sleep(2)
    print("done")
    print("if you want faster loading download premium edition")
    time.sleep(0.5)
    #init
os.system("cls" if os.name == "nt" else "clear")
print("-------------------------------------------------------------------------")
print()
print("-------------------------------------------------------------------------")
print()
print("-------------------------------------------------------------------------")
print()
print("-------------------------------------------------------------------------")
print()
print("-------------------------------------------------------------------------")
print()
print("-------------------------------------------------------------------------")
print()
print("-------------------------------------------------------------------------")
print()
print("-------------------------------------------------------------------------")
print()
print("-------------------------------------------------------------------------")
print()
print("-------------------------------------------------------------------------")
print()
print("-------------------------------------------------------------------------")
print()
print("-------------------------------------------------------------------------")
print()
print("-------------------------------------------------------------------------")
print()
print("-------------------------------------------------------------------------")
print("langue détectée : Français")
time.sleep(1)
if start_mode=="enable.premium":
    os.system("cls" if os.name == "nt" else "clear")
print()
print("-------------------------------------------------------------------------")

print("use the cls cmd for clear the screen")
print("program_killer=kill")


print("-------------------------------------------------------------------------")

time.sleep(1)
os.system("cls" if os.name == "nt" else "clear")
print("cmd executor")
print("premium enabled")
print("version +")
print("By : Clément BEYT")
time.sleep(0.3)
print("---------------------------")
print("Version : ", version)
print("Language : French (Fr) (France)")
print("Status : Stable")
print("Hidden cmd : Loaded")
print("Normal cmd : Loaded")
print("Police : Loaded")
print("Animations : Loaded")
print("Modules : Loaded")
print("Module list : random, os, time")
time.sleep(3)
os.system("cls" if os.name == "nt" else "clear")
print("---------------------------")
print("use the help cmd to get some informations")
print("---------------------------")

cmd = " "
historique = []

while cmd != "kill":
    cmd = input("enter commend here : ")

    if cmd != "":
        historique.append(cmd)

    if cmd == "help":
        print("liste des commandes :")
        print("[SPECIAL] [ADVENCED] : execute : execute python code")
        print("help : afficher ce menu")
        print("kill : terminer ce programme")
        print("clear : générer des lignes vides [!] après avoir fait cette commende tout se passe en bas de l'écran au lieu d'être en haut [!]")
        print("[!] SuperClear : la commande la plus puissante qui permet de générer des lignes pleines")
        print("cls : effacer réellement le terminal (Windows/Linux/Mac)")
        print("display_text : ouvrir l'invite d'affichage de texte")
        print("credit : affiche les crédits")
        print("test : lance une procédure de test d'affichage")
        print("calc : ouvre une mini calculatrice (+ - * /)")
        print("random : génère un nombre aléatoire")
        print("upper : convertit un texte en majuscules")
        print("lower : convertit un texte en minuscules")
        print("reverse : inverse une chaîne de caractères")
        print("count : compte les caractères d'un texte")
        print("history : affiche l'historique des commandes tapées")
        print("clear_history : vide l'historique des commandes")
        print("choice : choisit un élément au hasard dans une liste donnée")
        print("dice : lance un ou plusieurs dés")
        print("parrot : invoque un peroquet (il faut lui dire stop_exit pour le desinvoquer)")
        print("premium : open premium cmd invite")
        print("+ : open edition+ invite")
        print("si l'invite de commande est moddée il est possible que certaines commandes ne marchent plus")

    elif cmd == "cmd":
        print("cmd est le nom de la variable qui stoque les réponces a vaux tentative d'exécutions de commandes")

    elif cmd == "credit":
        print("super cmd executor premium +")
        print("version : ", version)
        print("Coder(s) :")
        print("- Clément BEYT")

    elif cmd == "credits":
        print("ERROR")

    elif cmd == "display_text":
        text_to_display = input("entre le texte a afficher : ")
        print("---------------------------")
        print(text_to_display)
        print("---------------------------")

    elif cmd == "":
        print("il faut renter une valeur dans l'invite")

    elif cmd == "test":
        time.sleep(0.3)
        print("---------------------")
        print("Testing Text")
        time.sleep(0.3)
        print("---------------------")
        print("0123456789")
        time.sleep(0.3)
        print("---------------------")
        print("azertyuiopqsdfghjklmwxcvbn")
        time.sleep(0.3)
        print("---------------------")
        print("AZERTYUIOPQSDFGHJKLMWXCVBN")
        time.sleep(0.3)
        print("---------------------")
        print("")
        time.sleep(0.3)
        print("---------------------")
        print(" ² & é ( - è _ ç à ) = , ; : ! < > | [ ] { # ~ ¤ % ù } + - * / . § ? ")
        time.sleep(0.3)
        print("---------------------")

    elif cmd == "calc":
        try:
            a = float(input("premier nombre : "))
            op = input("opérateur (+, -, *, /) : ")
            b = float(input("deuxième nombre : "))
            if op == "+":
                print("résultat :", a + b)
            elif op == "-":
                print("résultat :", a - b)
            elif op == "*":
                print("résultat :", a * b)
            elif op == "/":
                if b == 0:
                    print("ERROR : division par zéro impossible")
                else:
                    print("résultat :", a / b)
            else:
                print("ERROR : opérateur inconnu")
        except ValueError:
            print("ERROR : entrée invalide, il faut des nombres")

    elif cmd == "random":
        try:
            borne_min = int(input("borne minimale : "))
            borne_max = int(input("borne maximale : "))
            print("nombre généré :", random.randint(borne_min, borne_max))
        except ValueError:
            print("ERROR : il faut entrer des nombres entiers")

    elif cmd == "upper":
        texte = input("texte à convertir : ")
        print(texte.upper())

    elif cmd == "lower":
        texte = input("texte à convertir : ")
        print(texte.lower())

    elif cmd == "reverse":
        texte = input("texte à inverser : ")
        print(texte[::-1])

    elif cmd == "count":
        texte = input("texte à compter : ")
        print("nombre de caractères :", len(texte))
        print("nombre de mots :", len(texte.split()))

    elif cmd == "history":
        if len(historique) <= 1:
            print("aucune commande dans l'historique")
        else:
            print("historique des commandes :")
            for i, ancienne_cmd in enumerate(historique[:-1], start=1):
                print(f"{i}. {ancienne_cmd}")

    elif cmd == "clear_history":
        historique.clear()
        print("historique vidé")

    elif cmd == "choice":
        elements = input("entre des éléments séparés par des virgules : ")
        liste = [e.strip() for e in elements.split(",") if e.strip() != ""]
        if liste:
            print("élément choisi :", random.choice(liste))
        else:
            print("ERROR : aucune liste valide fournie")

    elif cmd == "dice":
        try:
            nb_des = int(input("nombre de dés à lancer : "))
            faces = int(input("nombre de faces par dé : "))
            resultats = [random.randint(1, faces) for _ in range(nb_des)]
            print("résultats :", resultats)
            print("total :", sum(resultats))
        except ValueError:
            print("ERROR : il faut entrer des nombres entiers")

    elif cmd == "cls":
        os.system("cls" if os.name == "nt" else "clear")

    elif cmd == "clear":
        for _ in range(37):
            print()

    elif cmd == "SuperClear":
        lignes_avant = ["------------------------------"] * 6
        lignes_avant.append("------Start Clearing----------")
        lignes_avant += ["------------------------------"] * 43
        lignes_avant.append("----------Hello World---------")
        lignes_avant += ["------------------------------"] * 50
        lignes_avant.append("------Bye World---------------")
        lignes_avant += ["------------------------------"] * 20
        for ligne in lignes_avant:
            print(ligne)

    elif cmd == "kill":
        print("Closing App...")
        print("Clearing Cache")
        time.sleep(1)
        print("Checking for updates")
        time.sleep(1)
        print("encrypting premium files")
        print("encrypting edition+ files")
        time.sleep(2)
        print("Deleting the window")
        time.sleep(1)
    elif cmd == "parrot":
        par_input="Bonjour"
        while par_input != "stop_exit":
            print("parrot : ", par_input)
            par_input=input("you : ")
    elif cmd=="[!]":
        print("-_-")
    elif cmd=="premium":
        print("Welcome in premium pannel")
        if start_mode=="enable.premium":
            new_premium_mode=input(" entre 1 pour garde le mode actuel ou entre 2 pour desactiver premium")
            if new_premium_mode=="2":
                start_mode="no_premium"
            elif new_premium_mode=="1":
                print("rien n'a changé")
            else:
                print("error")
        else:
            premium_code_input=input("enter a premium key : ")
            if premium_code_input=="premium.123":
                start_mode="enable.premium"
                print("premium enabled")
            else:
                print("wrong code")
            os.system("cls" if os.name == "nt" else "clear")

    elif cmd=="+":
        print("Edition+ is loading")
        time.sleep(1)
        plus_cmd=input("enter an Edition+ cmd : ")
        if plus_cmd=="+":
            print("lol")
        if plus_cmd=="help":
            print("for use every cmd you have to download the cmd exectuor +")
            print("list of cmd :")
            time.sleep(0.5)
            print("help : display this menu")
            print("+ : easter egg")
    elif cmd=="execute":
        print("be carefull, if you copy and paste code here verify it before pressing enter")
        code_execute=input("enter python code to execute : ")
        exec(code_execute)

    else:
        print(f"ERROR : commande '{cmd}' inconnue, tape 'help' pour voir la liste des commandes")