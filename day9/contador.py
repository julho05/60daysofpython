#Um contador que para quando um vlaor maximo for antigdo pelo usuario

def contador_personalizado():
    try:
        limite = int(input("Digite o valor maximo do contador: "))
        #funcao range criar uma lista de número apartir do 0 
        #até o valor definido pelo usuario
        limite = limite + 1
        for i in range(limite):
            print(i)
            if i == limite:
                print("Contador atingiu o limite")
                break
    except ValueError:
        print("Entrada invalida. Porfavor insira um numero inteiro.")

contador_personalizado()
