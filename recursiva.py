import time

def ContagemRecursiva(N:int):
    if(N == 0): print(0)
    else:
        time.sleep(1)
        print(N)
        ContagemRecursiva(N - 1)

valor = int(input("digite um número INTEIRO para fazer uma contagem regressia apartir dele: "))
ContagemRecursiva(valor)

