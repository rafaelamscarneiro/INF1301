'''
Autores:    Daniel Peralta (1811442)
            Felipe Meiga (2011460)
            Rafaela Carneiro (2011483)
'''
import random

__all__ = ['escolha_do_nivel', 'define_senha', 'compara']

def escolha_do_nivel(n):
    global nivel, lim
    nivel = n
    if nivel==1:
        lim=8
        pedras=4
    elif nivel==2:
        lim=10
        pedras=5
    elif nivel==3:
        lim=12
        pedras=6
    return (nivel,lim,pedras)

def define_senha(nivel,definida=0):
    global senha
    if definida != 0:     # nao é um jogo novo, a senha ja foi definida no jogo salvo
        senha= definida
        return senha
    senha=[]
    lCores = ['red','green','blue','yellow','pink','cyan'] # cores disponiveis para o nivel 1
    if nivel != 1:                                          # se nao for o nivel 1, tera mais cores
        lCores.append('brown')
        if nivel == 3:
            lCores.append('purple')
    for i in range(nivel+3):                    #define as cores no vetor com a senha aleatoriamente de acordo
        senha.append(random.choice(lCores))     #com as cores disponiveis para cada nivel       
    return senha
    
def compara(tentativa,progresso):       # compara a chave com a senha e monta o vetor progresso com a chave
    global pretas, brancas              # e a qtd de acertos (bolas pretas e brancas)
    c_senha = senha.copy()          
    c_tentativa=tentativa.copy()
    pretas=0
    brancas=0
    j = len(progresso)
    progresso.append([tentativa])
    for i in range(len(c_senha)):
        if c_tentativa[i]==c_senha[i]:
            pretas+=1
            c_tentativa[i]=0
            c_senha[i]=0
    for cor in c_tentativa:
        if cor==0:
            continue
        if cor in c_senha:
            c_senha.remove(cor)
            brancas+=1
    progresso[j].append((pretas,brancas))
    return progresso
