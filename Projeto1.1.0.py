import requests
import tkinter as tk
from tkinter import ttk

x = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,BTC-BRL")
Dic = x.json()

def cotUSD():
    USD = Dic['USDBRL']["bid"]
    USD = float(USD)
    USD = round(USD, 2)
    resposta.config(text=f"{USD} R$")

def cotBTC():
    BTC = Dic['BTCBRL']["bid"]
    BTC = float(BTC)
    BTC = round(BTC, 2)
    resposta.config(text=f"{BTC} R$")

def confirm():
    select = combo.get()
    if select == "BTC":
       cotBTC()
    elif select == "USD":
       cotUSD()

       

root = tk.Tk()
root.title("Cotação de moedas")
root.geometry("300x400")

#aparência
style = ttk.Style(root)
style.theme_use("clam")

root.configure(bg="#2e2e2e")  # Fundo da janela

style.configure("TLabel",
                background="#2e2e2e",  # Fundo escuro
                foreground="white",     # Texto branco
                font=("Arial", 12))

style.configure("TCombobox",
                fieldbackground="#2e2e2e",  # Fundo da combobox escuro
                background="#2e2e2e",       # Fundo da combobox escuro
                foreground="black",

                
                font=("Arial", 12))

style.configure("TButton",
                background="#2e2e2e",
                foreground="white",
                fieldbackground="#2e2e2e")

#Configuração de tamanho das colunas e espaços
for i in range(7):
    root.grid_rowconfigure(i, weight=1) 
for j in range(3):
    root.grid_columnconfigure(j, weight=1)

titulo = ttk.Label(root, text="Cotação de moedas", font=("Arial", 16))
titulo.grid(row=0, column=1, pady=20)

moedas = ["USD","BTC"]
combo = ttk.Combobox(root,values=moedas, state="readonly")
combo.set("Escolha uma moeda")
combo.grid(pady=20,column=1,row=1)

confirm = ttk.Button(root,text="confirmar",command=confirm)
confirm.grid(pady=20,column=1,row=2)

resposta = ttk.Label(root, text="", font=("arial",14))
resposta.grid(pady=10,column=1,row=5)






root.mainloop()
