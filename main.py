import random 
import pickle
vermelho = ("\033[1;31m" )
branco = (255, 255, 255)
print("Seja bem vindo ao gerador de senhas")

caracteres = 'abcdefghijklmnopqrstuvwABCDEFGHIJKLMNOPQRSTUVW!@#$%¨&*().,?0123456789'

vizualizar_senha = input ("Deseja vizualizar suas senhas anteriores 1- Sim, 0- Não:")
if vizualizar_senha =="1":
    try:
        with open ("senhas.pkl", "rb") as arquivo:
            senhas_salvas = pickle.load (arquivo)
        print("Aqui estão suas senhas anteriores:")
        for senha_salva in senhas_salvas:
            print(senha_salva)
    except FileNotFoundError:
        print('Nenhuma senha anterior econtrada.')
    print("\n")
while True:
    gerar = int(input ("Deseja gerar uma senha: 1- sim, 0- não"))
    if gerar == 0:
            print("Muito obrigado por usar nosso programa, suas senhas estarão salvas!")
            exit
            break
    elif gerar == 1:
        numero = int(input ("Quantidades de senhas para gerar:"))
        tamanho = int(input ("Qual tamanho da sua senha:"))

        print("\nAqui estão suas senhas:")

        senhas = []

        for _ in range (numero):
            senha = "".join(random.choice(caracteres)for _ in range (tamanho))
            senhas.append (senha)
            print(senha)

        salvar = input("pressione Enter para salvar")

        with open ("senhas.pkl", "wb") as arquivo:
            pickle.dump(senhas, arquivo)
        print("As senhas foram salvas com sucesso!")
    else: 
        print("Entrada inválida! Tente novamente.")