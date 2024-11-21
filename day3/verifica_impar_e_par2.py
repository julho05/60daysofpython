entrada = input('Digite um numero: ')

try: #tente rodar
    numero = int(entrada)
    if numero % 2 == 0:
        print('Numero par')
    else:
        print('Numero impar')

except ValueError:
    print('Você nao passou um numero inteiro')