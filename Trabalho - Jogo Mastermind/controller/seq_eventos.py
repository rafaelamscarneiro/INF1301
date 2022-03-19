'''
Autores:    Daniel Peralta (1811442)
            Felipe Meiga (2011460)
            Rafaela Carneiro (2011483)
'''
from view import desenha_canvas as draw
from model import regras_do_jogo as rules
from tkinter import *
from tkinter import messagebox

def menu(top):
    princi = Menu(top)
    opcoes=Menu(princi)
    opcoes.add_command(label='Sair sem salvar',command=exit)
    opcoes.add_command(label='Salvar jogo',command=lambda:salvarPartida(progresso))
    princi.add_cascade(label='Opcoes',menu=opcoes)
    top.configure(menu=princi)
    return

def changeState(btn,new_state):     # muda o estado de um botao
    btn['state']=new_state
    return

def abre_jogo(niv,lim,ped,progr=0):
    #print("1 coisa em abre_jogo: progresso=",progresso)
    global checar
    tab= Tk()               # criacao da janela principal
    tab.geometry('345x800')
    menu(tab)
    cnv = Canvas(tab,width=345,height=800,bg='lightblue') # canvas da janela principal
    cnv.bind('<ButtonRelease-1>',funcao)
    checar = draw.monta_tabuleiro(niv,lim,ped,cnv,tab) # botao usado para conferir se uma chave é a senha
    #print("dentro de abre_jogo, progresso=",progresso)
    if progr != 0:                          # isso significa que a funcao foi chamada para abrir uma partida salva anteriormente
        draw.montaJogoSalvo(cnv,niv,progr)
    cnv.pack()
    monta_tentativa()       # cria vetor para armazenar a primeira chave
    
    return
    
def defineVariables(n):                         # essa funcao recebe o nivel da partida e define os valores para limite de jogadas, qtd de pedras, 
    global nivel,lim,pedras,senha,progresso     # a senha e cria um vetor para armazenar o progresso da partida, de acordo com o nivel escolhido
    tupla = rules.escolha_do_nivel(n)
    nivel=tupla[0]
    lim=tupla[1]
    pedras=tupla[2]
    senha=rules.define_senha(nivel)
    progresso=[]
    return
        

def iniciar_novo_jogo():    # abre uma janela para o usuario escolher entre os niveis I, II e III, define as regras de acordo 
    janela = Tk()           # com o nivel escolhido pelo usuario e abre a janela principal
    janela.geometry('300x250')
    janela.config(bg='white')
    msg = Label(janela,bg='white',text='Escolha o nível da próxima partida',font='Courier 10 bold')
    msg.pack()
    nivelI = Button(janela, bg='lightblue',text='I',font='Times 24 bold',width=3,command=lambda:[janela.destroy(),defineVariables(1),abre_jogo(nivel,lim,pedras)])
    nivelI.pack()
    nivelII = Button(janela, bg='lightblue',text='II',font='Times 24 bold',width=3,command=lambda:[janela.destroy(),defineVariables(2),abre_jogo(nivel,lim,pedras)])
    nivelII.pack()
    nivelIII = Button(janela, bg='lightblue',text='III',font='Times 24 bold',width=3,command=lambda:[janela.destroy(),defineVariables(3),abre_jogo(nivel,lim,pedras)])
    nivelIII.pack()
    return

def janela_inicial():       # abre a janela inicial do jogo, onde o jogador escolhe iniciar uma nova partida ou continuar uma partida antiga
    ini = Tk()
    ini.geometry('400x200')
    ini.config(bg='white')
    l = Label(ini,bg='lightblue',text='BEM VINDO AO MASTERMIND',font='Courier 20 bold')
    l.pack()
    novoJogo = Button(ini,bg='lightpink',text='INICIAR NOVA PARTIDA',font='Courier 14 bold',command=lambda:[ini.destroy(),iniciar_novo_jogo()])
    # se o usuario escolher iniciar uma nova partida, abre uma janela para a escolha do nivel
    novoJogo.pack()
    continuar = Button(ini,bg='lightpink',text='CONTINUAR PARTIDA ANTERIOR',font='Courier 14 bold',state='disabled',command=lambda:[ini.destroy(),continuarPartida()]) #desabilitado na primeira jogada

    arq = open("jogo_salvo.txt","r") # se existe jogo salvo, o botao de continuar partida anterior fica habilitado
    if arq.readline() != '':
        changeState(continuar,'normal')
    arq.close()

    continuar.pack()
    mainloop()
    
    return

def funcao(evento):
    x=evento.x
    y=evento.y
    
    global cor, yf_linha, yi_linha, attempts, final_tab

    attempts=len(progresso)             #qtd de tentativas ate entao = tamanho do vetor com o progresso

    final_tab = 450+100*(nivel-1)       #final do tabuleiro

    yf_linha=final_tab-50*attempts      #limites da linha do tabuleiro
    yi_linha=yf_linha-50                #para cada tentativa

    if y >= final_tab:                                  #limitando onde fica a paleta de cores para
        cor = evento.widget.itemcget(CURRENT,'fill')    #definir a cor da pedra que o usuario escolheu
    
    if cor != '' and y<yf_linha and y>yi_linha:                 #limitando na linha da jogada atual  
        evento.widget.itemconfig(CURRENT,fill=cor)              #para posicionar uma pedra
        xi_linha=20
        for i in range(pedras):             # procura em qual posicao foi colocada a pedra
            if xi_linha < x < xi_linha+35:
                break
            xi_linha+=40
        tentativa[i]=cor                #preenche o vetor com as tentativas na posicao em que foi colocado no canvas
        print(tentativa)

        if 0 not in tentativa:          #se o vetor com as tentativas está preenchido de cores, habilita o botao para checar a chave
            changeState(checar,'normal')
            checar.configure(command=lambda:[rules.compara(tentativa,progresso),monta_tentativa(),
                                             draw.attemptResult(evento.widget,progresso[-1][1][0],progresso[-1][1][1],attempts,final_tab),
                                             changeState(checar,'disabled'),resultado(progresso,evento.widget)])
            # esse botao compara a chave com a senha; cria um novo vetor para armazenar a proxima chave; desenha as pedras pretas e brancas;
            # verifica se o usuario ganhou ou perdeu; e desabilita o botao            
    return    
        
def monta_tentativa():          # vetor para armazenar cada chave
    global tentativa
    tentativa=[]
    for i in range(pedras):
        tentativa.append(0)
    return

def salvarPartida(progresso):
    arq = open("jogo_salvo.txt", "w")
    niv = len(progresso[0][0])-3        #nivel = qtd de pedras da tentativa - 3 
    arq.write(str(niv)+'\n')            # 1 linha do arquivo tem o nivel da partida
    for tent in progresso:              # escreve as cores de cada linha do tabuleiro e a qtd de pedras pretas e brancas (respectivamente) dessa linha
        for cor in tent[0]:
            arq.write(cor+';')
        arq.write(str(tent[1][0])+';'+str(tent[1][1])+'\n')
    arq.write("senha;")         # sinalizando a linha do arquivo txt com a senha da partida salva (sempre sera a ultima)
    for cor in senha:           
        arq.write(cor+';')
    arq.close()
    return

def continuarPartida():
    global senha, lim, nivel, pedras, progresso 
    vet_senha=[]
    arq = open("jogo_salvo.txt","r")
    progresso = []
    nivel = arq.readline()        # nivel é a primeira linha do arquivo
    nivel = int(nivel)
    lim = rules.escolha_do_nivel(nivel)[1]      # definindo limite de jogadas e qtd de pedras
    pedras = rules.escolha_do_nivel(nivel)[2]   # da partida salva
    for linha in arq:
        lista = linha.split(';')
        if lista[0]=="senha":                   # monta o vetor senha com a senha da partida salva
            for cor in lista:
                vet_senha.append(cor)
            vet_senha.remove('')
            vet_senha.remove("senha")
            senha = rules.define_senha(nivel,vet_senha)
            break
        tup = (int(lista[-2]),int(lista[-1][0]))     # pedras pretas e brancas de cada tentativa
        lista.remove(lista[-1])
        lista.remove(lista[-1])
        progresso.append([lista,tup])
    arq.close()    
    abre_jogo(nivel,lim,pedras,progresso)   #abre a janela e o canvas da partida salva
    return 

def resultado(progresso,cnv): # envia mensagem ao final do jogo se ganhou ou perdeu
    if progresso[-1][1][0] == pedras:   # mesma qtd de bolas pretas e pedras
        messagebox.showinfo("Resultado","Voce venceu!",icon='info')
        draw.mostra_senha(cnv,pedras,nivel,senha)

    elif len(progresso)==lim:       # alcancou o limite de jogadas
        messagebox.showinfo("Resultado","Voce perdeu",icon='info')
        draw.mostra_senha(cnv,pedras,nivel,senha)
    
    return
