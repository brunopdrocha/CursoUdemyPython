"""
Exercício
Exiba os índices da lista
1 Maria
2 Helena
3 Luiz
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append("Bruno")

for indice in range(len(lista)):
    print(indice+1,lista[indice])