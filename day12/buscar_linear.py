def buscar_linear(lista, numero_procurado):
    """"
    Procurar um numero dentro de uma lista utilizado busca linear

    :param lista: lista de numeros
    :param numero_procurado: o numero que procurar
    """

    for i, numero in enumerate(lista): #funcao nativa do python enumarate
    #enumerate passa por cada item dentro de uma lista enquanto contabiliza
        if numero == numero_procurado:
            return i
    return -1
    
lista = [10,5,7,8,11,30,25]
numero_procurado = 50

buscando_numero = buscar_linear(lista, numero_procurado)
print(buscando_numero)

if buscando_numero != -1:
    print(f"o numero se encontra no indice: {buscando_numero}")
else:
    print("numero não encontrado")
