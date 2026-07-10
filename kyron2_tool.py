#!/usr/bin/env python3
import requests
import socket
import os

ip2 = requests.get("https://api.ipify.org").text


hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def voltar_menu():
    escolha = input("\nPressione ENTER para voltar ao menu ou digite 'exit' para sair: ")

    if escolha.lower() == "exit":
        print("Saindo...")
        exit()

print("KYRON2 TOOL\n")

user_correct = "justmeknow"
user = input("say ur password: ")

if user == user_correct:

    while True:
        limpar_tela()

        print('--- MAIN MENU ---')
        print('what u want to do?\n')
        print('a) count from 1 to 100')
        print('b) questionnaire about networking')
        print('c) which is my ip')
        print('exit) quit')

        user2 = input('\nchoose: ').lower()

        if user2 == 'a':
            limpar_tela()
            print("--- COUNTING ---")

            i = 1
            while i <= 100:
                print(i)
                i += 1

            voltar_menu()

        elif user2 == 'b':
            limpar_tela()
            print("--- NETWORKING QUESTIONNAIRE ---\n")
            print("WELCOME TO THE QUESTIONNAIRE ABOUT NETWORKING")
            print("ON THIS GAME YOU NEED TO SAY IF THE PHRASE IS TRUE OR FALSE")

            input("\nPress ENTER to start...")
            limpar_tela()

            choice_user = input('1) The OSI model is used on the Internet today? (t/f)\n').lower()

            if choice_user == 'f':
                print('u hit')
                input("Press ENTER...")
                limpar_tela()

                choice_user2 = input('2) TCP/IP model is used on the Internet? (t/f)\n').lower()

                if choice_user2 == 't':
                    print('nice u hit')
                    input("Press ENTER...")
                    limpar_tela()

                    choice_user3 = input('3) TCP is faster than UDP? (t/f)\n').lower()

                    if choice_user3 == 'f':
                        print('u hit!')
                        input("Press ENTER...")
                        limpar_tela()

                        choice_user4 = input('4) HTTPS uses encryption? (t/f)\n').lower()

                        if choice_user4 == 't':
                            print('u hit')
                        else:
                            print('u wrong')

                        voltar_menu()

                    else:
                        print('u bad')
                        voltar_menu()

                else:
                    print('u is badass')
                    voltar_menu()

            else:
                print('u miss')
                voltar_menu()

        elif user2 == 'c':
            limpar_tela()
            print("--- YOUR IP ---\n")
            print('a) which is my priv ip?')
            print('b) which is my pub ip?\n')
            user_ip = input('choice: ')
            if user_ip == 'a':
                limpar_tela()
                print(f'your ip private ip is{ip}')
                print('press ENTER ...')
                voltar_menu()
            elif user_ip == 'b':
                print(f'your ip public is {ip2}')
                print('press ENTER...')
                voltar_menu()
            else:
                print('ure dumb ?')

            voltar_menu()

        elif user2 == 'exit':
            print("Goodbye!")
            break

        else:
            print("Invalid option!")
            voltar_menu()

else:
    print('U DIDNT ENTER BOT')