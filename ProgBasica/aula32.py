"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = int(input("Informe o numero: "))

if numero == 0 :
    print ("0 N E PAR NEM IMPAR")
elif numero % 2 == 0:
    print("Numero Par")
else:
    print("Numero Impar")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 


Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = int(input("Informe a hora"))

if hora <= 11:
    print("bom dia")
elif 12>= hora <=17:
    print("boa tarde")
else:
    print("Boa noite")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Informe seu nome ")

caracteres = len(nome)

if caracteres <= 4 :
    print("Nome Curto")
elif caracteres == 5 or caracteres == 6 :
    print("Nome Normal")
else:
    print("Nome Longo")
