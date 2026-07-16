#!/usr/bin/env python3

import os
import socket
import requests
import random, string
import hashlib
import platform


try:
    ip2 = requests.get("https://api.ipify.org", timeout=5).text
except requests.RequestException:
    ip2 = "Não foi possível obter o IP público (sem conexão)"

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)



def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def voltar_menu():
    escolha = input(
        "\nPressione ENTER para voltar ao menu ou digite 'exit' para sair: "
    )
    if escolha.lower() == "exit":
        print("Saindo...")
        exit()





def contar_1_a_100():
    limpar_tela()
    print("--- COUNTING ---")
    for i in range(1, 101):
        print(i)
    voltar_menu()


def questionario_redes():
    limpar_tela()
    print("--- NETWORKING QUESTIONNAIRE ---\n")
    print("WELCOME TO THE QUESTIONNAIRE ABOUT NETWORKING")
    print("ON THIS GAME YOU NEED TO SAY IF THE PHRASE IS TRUE OR FALSE")

    input("\nPress ENTER to start...")
    limpar_tela()

    choice_user = input(
        "1) The OSI model is used on the Internet today? (t/f): "
    ).lower()

    if choice_user == "f":
        print("u hit")
        input("Press ENTER...")
        limpar_tela()

        choice_user2 = input(
            "2) TCP/IP model is used on the Internet? (t/f): "
        ).lower()

        if choice_user2 == "t":
            print("nice u hit")
            input("Press ENTER...")
            limpar_tela()

            choice_user3 = input("3) TCP is faster than UDP? (t/f): ").lower()

            if choice_user3 == "f":
                print("u hit!")
                input("Press ENTER...")
                limpar_tela()

                choice_user4 = input(
                    "4) HTTPS uses encryption? (t/f): "
                ).lower()

                if choice_user4 == "t":
                    print("u hit")
                else:
                    print("u wrong")
            else:
                print("u bad")
        else:
            print("u is badass")
    else:
        print("u miss")

    voltar_menu()


def informacoes_ip():
    limpar_tela()
    print("--- YOUR IP ---\n")
    print("a) which is my priv ip?")
    print("b) which is my pub ip?\n")

    user_ip = input("choice: ").lower()

    if user_ip == "a":
        limpar_tela()
        print(f"your private ip is {ip}")
        input("Press ENTER...")
        voltar_menu()
    elif user_ip == "b":
        limpar_tela()
        print(f"your public ip is {ip2}")
        input("Press ENTER...")
        voltar_menu()
    else:
        print("invalid option")
        voltar_menu()


def gerador_senhas():
    caracteres = string.ascii_letters + string.punctuation + string.digits
    limpar_tela()
    print("--- PASSWORD GENERATOR ---")
    p_user = int(input('How many digits do you want your password to have? '))
    limpar_tela()
    senha_forte = "".join(random.choices(caracteres, k=p_user))
    print(senha_forte)
    voltar_menu()


def gerador_hash():
    limpar_tela()
    print("--- HASH GENERATOR ---")
    print("Which hash do you want to generate?")
    print('1 - MD5 ')
    print('2 - SHA-1')
    print('3 - SHA-256')
    print('4 - SHA-512')

    opcao = input("\nchoice: ")
    limpar_tela()

    texto = input("Digite o texto: ")

    if opcao == "1":
        print("\nMD5:")
        print(hashlib.md5(texto.encode()).hexdigest())

    elif opcao == "2":
        print("\nSHA-1:")
        print(hashlib.sha1(texto.encode()).hexdigest())

    elif opcao == "3":
        print("\nSHA-256:")
        print(hashlib.sha256(texto.encode()).hexdigest())

    elif opcao == "4":
        print("\nSHA-512:")
        print(hashlib.sha512(texto.encode()).hexdigest())

    else:
        print("Opção inválida.")

    voltar_menu()


def dns_lookup():
    limpar_tela()
    print("--- DNS LOOKUP ---")
    dominio = input("Digite um domínio (ex: google.com): ")

    try:
        ip = socket.gethostbyname(dominio)

        limpar_tela()
        print("--- DNS LOOKUP ---\n")
        print(f"Domínio : {dominio}")
        print(f"IP       : {ip}")

    except socket.gaierror:
        print("Domínio inválido ou não encontrado.")

    voltar_menu()


def ping_host():
    limpar_tela()
    print("--- PING HOST ---")
    host = input("Digite o IP ou domínio: ")

    limpar_tela()
    print(f"Pingando {host}...\n")

    if platform.system() == "Windows":
        comando = f"ping -n 4 {host}"
    else:
        comando = f"ping -c 4 {host}"

    os.system(comando)

    voltar_menu()


def informacoes_sistema():
    limpar_tela()
    print("--- SYSTEM INFORMATION ---")
    hostname = socket.gethostname()
    ip_privado = socket.gethostbyname(hostname)
    ip_publico = requests.get("https://api.ipify.org").text

    print("--- SYSTEM INFORMATION ---\n")

    print(f"Hostname      : {hostname}")
    print(f"Sistema       : {platform.system()}")
    print(f"Versão        : {platform.release()}")
    print(f"Arquitetura   : {platform.machine()}")
    print(f"Processador   : {platform.processor()}")
    print(f"Python        : {platform.python_version()}")
    print(f"IP Privado    : {ip_privado}")
    print(f"IP Público    : {ip_publico}")

    voltar_menu()

def bin_hex():
    print("--- DATA ENCODER ---\n")

    tiktok = input('Enter a text (phrase) or a number: ')
    limpar_tela()

    print("--- DATA ENCODER ---\n")
    print("What do you wanna convert it to?\n")
    print("a) Binary")
    print("b) Hexadecimal\n")

    apple = input("Choice: ").lower()

    if apple == "a" or apple == "bin":
        if tiktok.isdigit():
            print(bin(int(tiktok)))
        else:
            print(" ".join(format(ord(letra), '08b') for letra in tiktok))

    elif apple == "b" or apple == "hex":
        if tiktok.isdigit():
            print(hex(int(tiktok)))
        else:
            print(" ".join(format(ord(letra), '02x') for letra in tiktok))

    else:
        print("Invalid option.")
    voltar_menu()


def port_scanner():
    limpar_tela()
    print("--- PORT SCANNER ---")

    host = input("Enter an IP or domain: ")

    limpar_tela()
    print(f"Scanning {host}...\n")

    ports = [20, 21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 3389, 8080]

    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((host, port))

        if result == 0:
            print(f"[OPEN] Port {port}")
        else:
            print(f"[CLOSED] Port {port}")

        s.close()

    voltar_menu()


print("KYRON2 TOOL\n")

user_correct = "justmeknow"
user = input("say ur password: ")

if user == user_correct:
    while True:
        limpar_tela()

        print("--- MAIN MENU ---")
        print("what u want to do?\n")
        print("a) Count from 1 to 100")
        print("b) Networking Questionnaire")
        print("c) IP Information")
        print("d) Password Generator")
        print("e) Hash Generator")
        print("f) Port Scanner")
        print("g) DNS Lookup")
        print("h) Ping Host")
        print("i) System Information")
        print("j) Data Encoder")
        print("exit) Quit")

        user2 = input("\nchoose: ").lower()

        if user2 == "a":
            contar_1_a_100()
        elif user2 == "b":
            questionario_redes()
        elif user2 == "c":
            informacoes_ip()
        elif user2 == "d":
            gerador_senhas()
        elif user2 == "e":
            gerador_hash()
        elif user2 == "f":
            port_scanner()
        elif user2 == "g":
            dns_lookup()
        elif user2 == "h":
            ping_host()
        elif user2 == "i":
            informacoes_sistema()
        elif user2 == "j":
            bin_hex()
        elif user2 == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid option!")
            input("\nPress ENTER to continue...")

else:
    print("U DIDNT ENTER BOT")
