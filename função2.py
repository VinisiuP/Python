# ////////////////////////////////////////////////////////////////////////////////////////////////////
#                             alunos: Vinicius Portela e Breno Henrique

import math

a = float(input("digite a coordenada X do canhão: "))
b = float(input("digite a coordenada Y do canhão: "))
c = float(input("digite a força do disparo em newtons: "))
d = float(input("digite o angulo de inclinação em graus: "))

# ////////////////////////////////////////////////////////////////////////////////////////////////////

#                           TABELA DE VALORES GLOBAIS :D (FAVOR NÃO APAGAR)

Xinicial = a
Yinicial = b
F = c
teta = d

m = 0.5
g = 10

# ////////////////////////////////////////////////////////////////////////////////////////////////////



# ////////////////////////////////////////////////////////////////////////////////////////////////////

# MEXE NÃO MANO PELO AMOR DE DEUS PF NÃO MEXE SÓ DEUS SABE COMO QUE FUNCIONOU, ENTÃO NÃO MEXE.

def VelocidadeInicial():
    F = c
    v0 = (F * 1) / m 
    return v0

# ////////////////////////////////////////////////////////////////////////////////////////////////////



# ////////////////////////////////////////////////////////////////////////////////////////////////////

# IRMÃO, EU JA DISSE, NÃO MEXE CARA, PFVR EU TE IMPORO NÃO MEXE.

def VelocidadeInicialVertical():
    anguloEmRadianos = math.radians(teta)
    senoDeTeta = math.sin(anguloEmRadianos)
    resultado1 = VelocidadeInicial() * senoDeTeta
    return resultado1

# ////////////////////////////////////////////////////////////////////////////////////////////////////
 


# ////////////////////////////////////////////////////////////////////////////////////////////////////

# CARA, EU JÁ DISSE, NÃO MEXE IRMÃO, EU NÃO VOU DIZER DNV, PARA!

def VelocidadeinicialHorisontal():
    anguloEmRadianos = math.radians(teta)
    CosDeTeta = math.cos(anguloEmRadianos)
    resultado2 = VelocidadeInicial() * CosDeTeta
    return resultado2

# ////////////////////////////////////////////////////////////////////////////////////////////////////



# ////////////////////////////////////////////////////////////////////////////////////////////////////

# BRO, DONT MUDE NOTHING OK????? DONT MUDE NOTHING OR I VOU TE CATCH!

def TempoMaximo():
    Tmax = (2 * (VelocidadeinicialHorisontal() / g))
    return Tmax

# ////////////////////////////////////////////////////////////////////////////////////////////////////



# ////////////////////////////////////////////////////////////////////////////////////////////////////

# Mein Sohn, entferne dich jetzt von diesem Kodex. Ich weiß nicht, wo du wohnst, aber ich werde es herausfinden und zu deinem Haus gehen, nur um dir eine Ohrfeige zu geben

def Tempo():
    Temp = TempoMaximo() / 2
    return  Temp

# ////////////////////////////////////////////////////////////////////////////////////////////////////



# ////////////////////////////////////////////////////////////////////////////////////////////////////

# Ei se mecher aqui é pq tu quer da o quê... não irei completar. Não estou zuando. Realmente não mecha -Waldyr (ele escreveu mexa errado KKKKKKKK)

def VelocidadeX():
    Vx = VelocidadeinicialHorisontal()
    return Vx

# ////////////////////////////////////////////////////////////////////////////////////////////////////



# ///////////////////////////////////////////////////////////////////////////////////////////////////

# Please, dont make anything here, this code is ready and if u make anything u will die before the christmas - Chrisdtian

def VelocidadeY():
    Vy = (VelocidadeInicialVertical() - (g * Tempo()))
    return Vy

# ////////////////////////////////////////////////////////////////////////////////////////////////////



# ////////////////////////////////////////////////////////////////////////////////////////////////////

# eu tô com medo mano, não mexe, a gnt já tá na linha 131. Não mexe por favor.

def IpisilonMax():
    Ymax = (Yinicial + (VelocidadeInicialVertical() * Tempo)) - ((g * (Tempo ** 2)) / 2 )
    return Ymax

# ////////////////////////////////////////////////////////////////////////////////////////////////////



# ////////////////////////////////////////////////////////////////////////////////////////////////////

# 😿😿 PARA...

def XisMax():
    Xmax = (Xinicial + (VelocidadeinicialHorisontal() * TempoMaximo))
    return Xmax

# ////////////////////////////////////////////////////////////////////////////////////////////////////



# ////////////////////////////////////////////////////////////////////////////////////////////////////

input("Pressione ENTER para receber os resultados do lançamento")

print(f"A velocidade inicial do lançamento foi de: {VelocidadeInicial()} metros")
input()

print(f"O tempo total do voo do projétil foi de:  {Tempo():.2f} segudos")
input()

# ////////////////////////////////////////////////////////////////////////////////////////////////////

PosicoesInstanteX = []
PosicoesInstanteY = []

for t in range(int(TempoMaximo()) + 1):
    posicaoX = Xinicial + VelocidadeX() * t
    posicaoY = Yinicial + VelocidadeInicialVertical() * t - 0.5 * g * t ** 2
    PosicoesInstanteX.append(posicaoX)
    PosicoesInstanteY.append(posicaoY)

print(f"As posições de X e Y em cada instante do voo foram: ")
for t, (posicaoX, posicaoY) in enumerate(zip(PosicoesInstanteX, PosicoesInstanteY)):
    print(f"Tempo {t}: Posição X = {posicaoX:.3f}, Posição Y = {posicaoY:.3f}")

# ////////////////////////////////////////////////////////////////////////////////////////////////////