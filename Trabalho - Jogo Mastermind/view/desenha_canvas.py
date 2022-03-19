'''
Autores:    Daniel Peralta (1811442)
            Felipe Meiga (2011460)
            Rafaela Carneiro (2011483)
'''
from tkinter import *
import random

def mostra_senha(cnv,pedras,nivel,senha,xi=20,xf=50,teste=False):      # define a senha e monta ela na parte de cima do tabuleiro(onde fica a senha escondida durante o jogo)
    for cor in senha:
        o = cnv.create_oval(xi,20,xf,50,outline=cor,fill=cor)
        xi = xf+10
        xf = xi+30
    return 

def esqueleto(cnv,xi,yi,xf,yf,pedras,linhas):           # monta os retangulos para colocar as chaves e os resultados
    altura=yf-yi
    r = cnv.create_rectangle(5,yi,340,yf,outline='black',state='disabled')   # cria o primeiro retangulo
    for cont in range(pedras):                                               # preenche o primeiro retangulo com a chave escondida
        o = cnv.create_oval(xi,20,xf,50,outline='grey',fill='grey')
        xi = xf+10
        xf = xi+30
    yi=yf
    yf+=altura
    cont=0
    while cont < linhas:                                    #cria os retangulos restantes
        r = cnv.create_rectangle(5,yi,270,yf,outline='black',state='disabled')      
        q = cnv.create_rectangle(270,yi,340,yf,outline='black',state='disabled') 
        yi=yf
        yf+=altura
        cont+=1
    global fim_tab
    fim_tab=yf-altura                                       #coordenada y do final do tabuleiro, vai ser usada na funcao paleta_de_cores()
    return

def circulos(cnv,xi,yi,xf,yf,pedras,linhas):        #coloca os circulos em cada linha do tabuleiro
    const_xi = xi
    const_xf = xf
    i=0
    while i<linhas:
        for cont in range(pedras):
            o = cnv.create_oval(xi,yi,xf,yf,outline='grey',fill='white')
            xi = xf+10
            xf = xi+30
        xi = const_xi
        xf = const_xf
        yi=yf+20
        yf=yi+30
        i+=1
    return

def paleta_de_cores(cnv,xi,xf,nivel):               # monta a paleta de cores
    lCores = ['red','green','blue','yellow','pink','cyan'] #cores disponiveis no nivel 1
    if nivel != 1:                                          # se nao for nivel 1, acrescenta cor(es)
        lCores.append('brown')
        if nivel == 3:
            lCores.append('purple')
    i=0
    cont=0
    yi = fim_tab+10         # a paleta de cores vai ser posicinada abaixo do final do tabuleiro
    yf = yi+30
    while cont < len(lCores):   # define a paleta e posiciona
        o = cnv.create_oval(xi,yi,xf,yf,outline=lCores[i],fill=lCores[i])
        xi=xf+10
        xf=xi+30
        i+=1
        cont+=1
    return yf       # retorna a ordenada final, usada para posicionar o botao de checagem da chave


def monta_tabuleiro(nivel, lim, pedras,cnv,tab):    # monta todo o tabuleiro, utilizando as funçoes acima
    esqueleto(cnv,20,10,50,60,pedras,lim)
    yf = paleta_de_cores(cnv,20,50,nivel)
    circulos(cnv,20,70,50,100,pedras,lim)
    checar = Button(tab,text="Checar",bg='orange',font='Courier 24 bold',state='disabled')    # botao para o usuario testar uma chave
    checar.place(x=100,y=yf+4)      # posiciona o botao abaixo da paleta de cores
    return checar

def attemptResult(cnv,pretas,brancas,linha,final_tab):      # verifica a qtd de acertos da tentativa
    xi=280
    yi=final_tab-35
    yi-=linha*50
    i=0
    for i in range(pretas):         # desenha as bolas pretas
        if i==4:
            yi+=15
            xi=280
        o = cnv.create_oval(xi,yi,xi+10,yi+10,outline='black',fill='black')
        xi+=15
    for j in range(brancas):        # desenha as bolas brancas
        if j==4 or j+i==3:
            yi+=15
            xi=280
        o = cnv.create_oval(xi,yi,xi+10,yi+10,fill='white')
        xi+=15
    cnv.pack()
    return

def montaJogoSalvo(cnv,nivel,progr):        # desenha o jogo salvo anteriormente qdo o usuario escolhe continuar a partida salva
    final_tab = 450+100*(nivel-1)
    yi = final_tab
    xi = 20
    for tent in progr:        
        for cor in tent[0]:
            o = cnv.create_oval(xi,yi,xi+30,yi-30,outline=cor,fill=cor)
            xi+=40
        xi=20
        pretas=tent[1][0]
        brancas=tent[1][1]
        attemptResult(cnv,pretas,brancas,0,final_tab)
        yi-=50
        final_tab-=50
    return
    















