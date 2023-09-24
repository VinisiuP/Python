#NÃO ESTA EM ORODEM


# perguntas = ["é bolsonaro ou não é?",
#              "o ceu é azul?",
#              "faz o L?",
#              "o céu é rosa",
#              "leo lins é bala",
#              "orgulho de ser sesi?",
#              "cabo de santo agostinho é fim de mundo?",
#              "biruleibileibe",
#              "ai neymar"]

# respostas = ["é",
#              "tecnicamente sim",
#              "FAZ O L",
#              "não",
#              "mto",
#              "nem um pouco",
#              "pra caramba",
#              "a ti toma no",
#              "gosta de bater né"]

# x = 0 

# for i in range(len(perguntas)):
#     resposta = input(perguntas[i])
#     if (resposta.lower() == respostas[i]):
#         print('macaco esperto')  
#         x = x + 1
#     else:
#        print("macaco burro")

# products = ["açucar", "feijão","macarrão"]
# stock = ["27","50","12"]
# price = ["25","10","30"]
# concluir = False

# while (not concluir):
#     print("Digite o nome do produto:")
#     nomeProduto = input()
#     print("Digite o estoque do produto")
#     estoqueProduto = float(input())
#     if(estoqueProduto < 15): print("tá falntando produto")
#     elif(estoqueProduto < 10): print("acaba daqui a pouco")
#     else: print("tá tudo jóia")
#     print("Digite o preço do produto")
#     preçoProduto = float(input())

#     products.append(nomeProduto)
#     stock.append(estoqueProduto)
#     price.append(preçoProduto)

#     print("Deseja inserir outra informação?(s/n)")
#     concluir = input() == "n"

# print(f"Abaixo pode ser visto as informações do produto:")
# print(f"produto : estoque do produto : preço do produto")
# for i in range(len(products)):
#     print(f"{products[i]} : {stock[i]} : R${price[i]}")

 #input("Pressione Enter pra terminar...")

# produtos = []
# estoque = []
# preço = []

# concluir = False

# while (not concluir):
#     print("Digite o nome do prodto:")
#     nomeproduto = input()
#     print("Digite a quantidade do produto")
#     estoqueproduto = int(input())
#     print("Digite o preço do produto")
#     preçoproduto = float(input())

#     produtos.append(nomeproduto)
#     estoque.append(estoqueproduto)
#     preço.append(preçoproduto)

#     print("Deseja inserir outr produto?(s/n)")
#     concluir = input() == "n"

# print("Seguem abaixo todas os produtos, quantidades e preços digitadas:")
# print("produto : quantidade : preço")
# for i in range(len(produtos)):
#     print(f"{produtos[i]} : {estoque[i]} : {preço[i]}")

# input("Pressione Enter pra terminar...")

# filename = "ARQUIOVOBALA.txt"
# file = open(filename, 'w')
# for i in range(len(produtos)):
#     outputline = f"NOME DO PRODUTO: {produtos[i]}\n QUANTIDADE: {estoque[i]}\n VALOR: R${preço[i]}\n"  
#     file.write(outputline)
# file.close()

# função
# definição, subrotina, método, procedimento
# Caucula a media entre dois valores, EX: a e b
# def media(a,b):
#     s = a + b
#     m = s / 2
#     return m
# print(media(7,8))

# def mediaponderada(a, b, pa, pb):
#     s = apa + ppb
#     p = pa + pb 
#     m = s / p
#     return m 
# print(media(7,8))
# print(mediaponderada)

def media(c:float,d:float):
     soma = c + d
     m = soma / 2
     return m

print("CALCULADOR DE MEDIAS 3000 PRO (SEM VIRUS) 2023 EVOLUTION\n ")

c = float(input("Digite a primeira nota: "))
d = float(input("Digite a segunda nota: "))
print(f"a média desse aluno é: {media(c,d):.2f}")