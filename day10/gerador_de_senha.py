import random
import string

#random fornece para gerar números aleatorios 
#string fornece um conjunto de caracteres prontos
#como letra maísuclas, numeros e simbolos 

def gerador_de_senhas(tamanho):
    comprimento = tamanho
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''

    while len(senha) < comprimento :
        senha += random.choice(caracteres)

    print(f"Sua senha ficou assim: {senha}")

gerador_de_senhas(10)

