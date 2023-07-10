import random 
vermelho = ("\033[1;31m" )
print("Seja bem vindo ao gerador de senhas")

caracteres = 'abcdefghijklmnopqrstuvwABCDEFGHIJKLMNOPQRSTUVW!@#$%¨&*().,?0123456789'

numero = input ("Quantidades de senhas para gerar:")
numero= int(numero)

tamanho = input ("Qual tamanho da sua senha:")
tamanho = int(tamanho)

print("\nAqui estão suas senhas:")

for pwd in range (numero):
    senhas = ""
    for c in range (tamanho):
        senhas += random.choice(caracteres)
    print(vermelho, senhas)