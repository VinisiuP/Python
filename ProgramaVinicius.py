# Escrever aqui coisas só pra lembrar :D (comentários)

my_age = input("Quantos anos você tem?")
idade = int(my_age)
print("você tem", idade, "anos.")
if idade >=18:
    print("e você já pode ser preso")
    curso_superior = input("você tem curso superior?")
    if curso_superior == "sim":
       print("então você direito a uma cela especial")
    else:
        print("você vai ficar com os outros presos normais E NU!")
else:
    print("então você ainda não pode ser preso")
if idade <0:
    print("porém sua idade é invalida")




