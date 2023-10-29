"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input ('Seu nome')
idade = input ('Sua Idade')

if nome and idade != (""):
    print (f' seu nome {nome}')
    print('Nome invertido ',nome[::-1])
    if nome  not in "":
        print("Seu nome tem espaco")
    print (len(nome))
    print ("Primeira Letra",nome[0])
    print ("Ultima Letra",nome[-1])
else:
    print("Nada foi digitado")