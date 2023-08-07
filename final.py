import random 
import pickle 
import tkinter as tk
from tkinter import messagebox 

caracteres = 'abcdefghijklmnopqrstuvwABCDEFGHIJKLMNOPQRSTUVW!@#$%¨&*().,?0123456789'

def gerar_senha():
    try:
        numero = int(numero_entry.get())
        tamanho = int(tamanho_entry.get())
    except ValueError:
        messagebox.showerror('Erro', 'Por favor, insira números válidos!')
        return
    senhas = ["".join(random.choice(caracteres) for _ in range(tamanho)) for _ in range(numero)]
    with open("Senhas.pkl", "wb") as arquivo:
        pickle.dump(senhas,arquivo)
    messagebox.showinfo("Sucesso", "As senhas foram salvas com sucesso!")

def vizualizar_senhas():
    try:
        with open ("senhas.pkl", "rb") as arquivo:
            senhas_salvas = pickle.load(arquivo)
        messagebox.showinfo("Senhas salvas", "\n".join(senhas_salvas))
    except FileNotFoundError:
        messagebox.showerror("Erro", "Nenhuma senha ecnotrada.")
root = tk.Tk()
root.title("Gerador de senhas")
welcome_label = tk.Label(root, text="Seja bem vindo ao gerador de senhas!")
welcome_label.pack
visualizar_button = tk.Button(root, text="Visualizar senhas salvas", command=vizualizar_senhas)
visualizar_button.pack()
numero_label = tk.Label(root, text="Quantas senhas você deseja gerar?")
numero_label.pack()

numero_entry = tk.Entry(root)
numero_entry.pack()

tamanho_label = tk.Label(root, text="Qual o tamanho da senha?")
tamanho_label.pack()

tamanho_entry = tk.Entry(root)
tamanho_entry.pack()

gerar_button = tk.Button(root, text="Gerar senha", command=gerar_senha)
gerar_button.pack()

root.mainloop()