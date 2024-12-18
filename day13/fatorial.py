#O que é um faotiral?
#É um calculo em matematica que multipicamos os valores a partir do numero passado
#Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120


def fatorial(n):
    """
    Calcula o fatorial de um número usando recursão
    :param n: número inteiro não negativo
    :return: fatorial de n.
    """

    if n < 0:
        raise ValueError("O numero deve ser positivo")
    
    #então esse condicinal retorna 1 se o caso o numero da função for 0 ou 1
    if n == 0 or n == 1:
        return 1
    
    return n * fatorial(n - 1)