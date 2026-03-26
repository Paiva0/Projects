import os
import hashlib
import stdiomask
import requests
import secrets
from usersDiogoPaivaPI06 import users
import tkinter as tk
import math
 
from dotenv import load_dotenv
 
load_dotenv()
 
TELEGRAM_BOT_TOKEN = (os.getenv("TELEGRAM_BOT_TOKEN") or "").strip()
TELEGRAM_CHAT_ID = (os.getenv("TELEGRAM_CHAT_ID") or "").strip()
 
 
def Inicio():
    cls()
    print("Bem-vindo a calculadora!")
 
    # CORREÇÃO: variáveis no escopo correto de Inicio()
    tempNumb = 0.0
    tempNumb2 = 0.0
    tempOperator = ""
 
    # CORREÇÃO: uma única função para todos os dígitos em vez de 10 funções repetidas
    def add_digit(n):
        nonlocal tempNumb, tempNumb2, tempOperator
        current = lbl_text["text"]
        if current == "0":
            lbl_text["text"] = str(n)
        else:
            lbl_text["text"] = current + str(n)
 
    def add_point():
        if "." not in lbl_text["text"]:
            lbl_text["text"] = lbl_text["text"] + "."
 
    # CORREÇÃO: nonlocal em vez de global
    def add():
        nonlocal tempNumb, tempNumb2, tempOperator
        if lbl_text["text"] != "0":
            tempNumb = float(lbl_text["text"])
            lbl_text["text"] = "0"
            tempOperator = "+"
 
    def minus():
        nonlocal tempNumb, tempNumb2, tempOperator
        if lbl_text["text"] != "0":
            tempNumb = float(lbl_text["text"])
            lbl_text["text"] = "0"
            tempOperator = "-"
 
    def divide():
        nonlocal tempNumb, tempNumb2, tempOperator
        if lbl_text["text"] != "0":
            tempNumb = float(lbl_text["text"])
            lbl_text["text"] = "0"
            tempOperator = "/"
 
    def multi():
        nonlocal tempNumb, tempNumb2, tempOperator
        if lbl_text["text"] != "0":
            tempNumb = float(lbl_text["text"])
            lbl_text["text"] = "0"
            tempOperator = "*"
 
    # CORREÇÃO: try/except para raiz de número negativo
    def sqr():
        try:
            valor = float(lbl_text["text"])
            if valor < 0:
                lbl_text["text"] = "Erro"
            else:
                resultado = math.sqrt(valor)
                lbl_text["text"] = str(resultado)
        except ValueError:
            lbl_text["text"] = "Erro"
 
    def clear():
        lbl_text["text"] = "0"
 
    def per():
        if lbl_text["text"] != "0":
            try:
                lbl_text["text"] = str(float(lbl_text["text"]) / 100)
            except ValueError:
                lbl_text["text"] = "Erro"
 
    def equal():
        nonlocal tempNumb, tempNumb2, tempOperator
        if lbl_text["text"] == "0" or tempOperator == "":
            return
        try:
            tempNumb2 = float(lbl_text["text"])
 
            if tempOperator == "+":
                result = tempNumb + tempNumb2
            elif tempOperator == "-":
                result = tempNumb - tempNumb2
            elif tempOperator == "/":
                if tempNumb2 == 0:
                    lbl_text["text"] = "Erro /0"
                    lbl_History["text"] = ""
                    return
                result = tempNumb / tempNumb2
            elif tempOperator == "*":
                result = tempNumb * tempNumb2
            else:
                return
 
            # CORREÇÃO: historico agora é atualizado corretamente via nonlocal
            historico = f"{tempNumb} {tempOperator} {tempNumb2} = {result}"
            lbl_History["text"] = historico
 
            # Mostrar inteiro se não tiver casas decimais
            if result == int(result):
                lbl_text["text"] = str(int(result))
            else:
                lbl_text["text"] = str(result)
 
            tempOperator = ""
 
        except ValueError:
            lbl_text["text"] = "Erro"
 
    # --- Interface gráfica ---
    window = tk.Tk()
    window.title("Calculator")
 
    window.rowconfigure([0, 1, 2, 3, 4, 5, 6], minsize=100, weight=1)
    window.columnconfigure([0, 1, 2, 3], minsize=100, weight=1)
 
    # CORREÇÃO: font correto ("Arial", tamanho) em vez de font=(100)
    FONT = ("Arial", 18)
    FONT_DISPLAY = ("Arial", 24, "bold")
    FONT_HISTORY = ("Arial", 12)
 
    lbl_History = tk.Label(window, text="", font=FONT_HISTORY, anchor="e")
    lbl_History.grid(row=0, column=0, columnspan=4, sticky="nsew")
 
    lbl_text = tk.Label(window, text="0", font=FONT_DISPLAY, anchor="e")
    lbl_text.grid(row=1, column=0, columnspan=4, sticky="nsew")
 
    # Botões de operação
    tk.Button(window, text="AC",  font=FONT, command=clear).grid(row=2, column=0, sticky="nsew")
    tk.Button(window, text="sqr", font=FONT, command=sqr).grid(row=2, column=1, sticky="nsew")
    tk.Button(window, text="%",   font=FONT, command=per).grid(row=2, column=2, sticky="nsew")
    tk.Button(window, text="-",   font=FONT, command=minus).grid(row=2, column=3, sticky="nsew")
 
    # CORREÇÃO: lambda para passar argumento à função única add_digit()
    tk.Button(window, text="7", font=FONT, command=lambda: add_digit(7)).grid(row=3, column=0, sticky="nsew")
    tk.Button(window, text="8", font=FONT, command=lambda: add_digit(8)).grid(row=3, column=1, sticky="nsew")
    tk.Button(window, text="9", font=FONT, command=lambda: add_digit(9)).grid(row=3, column=2, sticky="nsew")
    tk.Button(window, text="+", font=FONT, command=add).grid(row=3, column=3, sticky="nsew")
 
    tk.Button(window, text="4", font=FONT, command=lambda: add_digit(4)).grid(row=4, column=0, sticky="nsew")
    tk.Button(window, text="5", font=FONT, command=lambda: add_digit(5)).grid(row=4, column=1, sticky="nsew")
    tk.Button(window, text="6", font=FONT, command=lambda: add_digit(6)).grid(row=4, column=2, sticky="nsew")
    tk.Button(window, text="/", font=FONT, command=divide).grid(row=4, column=3, sticky="nsew")
 
    tk.Button(window, text="1", font=FONT, command=lambda: add_digit(1)).grid(row=5, column=0, sticky="nsew")
    tk.Button(window, text="2", font=FONT, command=lambda: add_digit(2)).grid(row=5, column=1, sticky="nsew")
    tk.Button(window, text="3", font=FONT, command=lambda: add_digit(3)).grid(row=5, column=2, sticky="nsew")
    tk.Button(window, text="*", font=FONT, command=multi).grid(row=5, column=3, sticky="nsew")
 
    tk.Button(window, text="0", font=FONT, command=lambda: add_digit(0)).grid(row=6, column=0, columnspan=2, sticky="nsew")
    tk.Button(window, text=".", font=FONT, command=add_point).grid(row=6, column=2, sticky="nsew")
    tk.Button(window, text="=", font=FONT, command=equal).grid(row=6, column=3, sticky="nsew")
 
    window.mainloop()
 
 
def pause():
    input("Pressione Enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')
 
 
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
 
 
def save_users():
    with open("usersDiogoPaivaPI06.py", "w") as f:
        f.write("users = {\n")
        for username, data in users.items():
            f.write(f'    "{username}": {{\n')
            f.write(f'        "salt": "{data["salt"]}",\n')
            f.write(f'        "hash": "{data["hash"]}"\n')
            f.write(f'    }},\n')
        f.write("}\n")
 
 
def register():
    cls()
    print("Registrar novo utilizador")
    username = input("Username: ").strip()
 
    if username in users:
        print("Username já existe.")
        pause()
        return
 
    password = stdiomask.getpass("Password: ", mask=" ")
    salt = os.urandom(16).hex()
    hashed = hashlib.sha256((salt + password).encode("utf-8")).hexdigest()
 
    users[username] = {"salt": salt, "hash": hashed}
    save_users()
    print(f"Utilizador '{username}' registado com sucesso!")
    pause()
 
 
def login():
    while True:
        cls()
        print("Faça o seu login")
        username = input("Username: ").strip()
 
        if username not in users:
            print("Username não encontrado.")
            pause()
            continue
 
        while True:
            password = stdiomask.getpass("Password: ", mask=" ")
 
            stored_salt = users[username]["salt"]
            stored_hash = users[username]["hash"]
 
            attempt = hashlib.sha256((stored_salt + password).encode("utf-8")).hexdigest()
 
            if attempt == stored_hash:
                twofa_code = f"{secrets.randbelow(10000):04d}"
                send_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
                payload = {
                    "chat_id": TELEGRAM_CHAT_ID,
                    "text": f"O teu código de autenticação é: {twofa_code} seu anormal"
                }
                try:
                    req = requests.post(send_url, json=payload, timeout=10)
                    req.raise_for_status()
                except requests.RequestException as e:
                    print(f"Erro ao enviar código Telegram: {e}")
                    return False
 
                cls()
                print("Login bem-sucedido! Código enviado para o Telegram.")
                login_code = input("Insira o código de autenticação: ").strip()
 
                if login_code == twofa_code:
                    print("Autenticação bem-sucedida!")
                    Inicio()
                    return True
                else:
                    print("Código de autenticação incorreto. Burro.")
                    break
            else:
                print("Password incorreta. Tente novamente.")
 
 
def menu():
    while True:
        print("1. Login")
        print("2. Registrar")
        print("3. Sair")
        choice = input("Escolha uma opção: ").strip()
 
        if choice == "1":
            if login():
                break
        elif choice == "2":
            register()
        elif choice == "3":
            print("A saír...")
            break
        else:
            print("Opção inválida. Tente novamente.")
 
 
def main():
    menu()
 
 
main()
