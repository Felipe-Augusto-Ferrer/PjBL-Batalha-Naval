import time
import sys
import random
import os

#Tempo da narração (introdução)
def narracao(texto, atraso=0.07):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(atraso)
    print()

#Introdução
def introducao():
    print()
    narracao("BATALHA NAVAL")
    print()
    time.sleep(1.2)

    narracao("Ano: 1942")
    time.sleep(1.2)
    narracao("Oceano Atlântico Sul - 03:42 da madrugada")
    time.sleep(1.5)

    os.system('cls')

    print()
    narracao("*O som das ondas colidindo contra o casco de aço é a única coisa real.*")
    narracao("*Lá fora, uma névoa espessa e escura engoliu o horizonte.*")
    narracao("*Você não enxerga a proa do seu próprio navio.*")
    time.sleep(1.2)

    os.system('cls')

    print()
    narracao("*Na sala de comando, as luzes brancas foram apagadas.*")
    narracao("*Resta apenas o brilho vermelho e estático dos painéis de emergência.*")
    narracao("*O operador do radar se vira para você. O rosto dele está pálido.*")
    time.sleep(1.5)
    print()
    narracao("-Comandante... o radar parou de responder. Pane geral. Estamos cegos.")
    time.sleep(1.5)

    os.system('cls')

    print()
    narracao("*Você caminha até a mesa tática. O silêncio na sala é sufocante.*")
    narracao("*Você sabe que, em algum lugar desse quadrante escuro, ELES estão caçando você.*")
    narracao("*Porta-aviões, cruzadores, submarinos... fantasmas de metal escondidos no nevoeiro.*")
    time.sleep(1.2)

    print()
    narracao("*Se você se mover, revelará sua posição.*")
    narracao("*Se ficar parado, será um alvo fácil.*")
    time.sleep(1.2)

    os.system('cls')

    print()
    narracao("*O oficial de armas destrava o painel de artilharia pesada.*")
    narracao("*Os canhões estão carregados. O metal range com a pressão hidráulica.*")
    time.sleep(1.2)
    
    print()
    narracao("*Todos os olhos da sala de comando se voltam para você.*")
    narracao("*Eles esperam sua ordem. Sua mente é a única arma que restou.*")
    time.sleep(1.5)

    os.system('cls')

    print()
    narracao("-Prontos para disparar, Senhor. Diga-nos para onde apontar...")
    time.sleep(1.2)

    print()
    narracao("...",1.5)
    time.sleep(2.0)

    os.system('cls')

    print()
    narracao("---SUA MISSÃO: Deduzir as coordenadas e estraçalhar a frota inimiga.")
    narracao("               Um erro... e o seu navio será o próximo a afundar.")
    
    time.sleep(1.0)
    print()
    print()
    narracao("Você está pronto?")
    print()
    time.sleep(1.0)

#Tabuleiro 5x10
def modoFacil():
    tabuleiro=[
        ["🟦","1️⃣ ","2️⃣ ","3️⃣ ","4️⃣ ","5️⃣ ","6️⃣ ","7️⃣ ","8️⃣ ","9️⃣ ","🔟"],
        ["1️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["2️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["3️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["4️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["5️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"]
    ]
    return tabuleiro

    tabuleiroInimigo=[
        ["🟦","1️⃣ ","2️⃣ ","3️⃣ ","4️⃣ ","5️⃣ ","6️⃣ ","7️⃣ ","8️⃣ ","9️⃣ ","🔟"],
        ["1️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["2️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["3️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["4️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["5️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"]
    ]
    return tabuleiroInimigo

    tabuleiroVisual=[
        ["🟦","1️⃣ ","2️⃣ ","3️⃣ ","4️⃣ ","5️⃣ ","6️⃣ ","7️⃣ ","8️⃣ ","9️⃣ ","🔟"],
        ["1️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["2️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["3️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["4️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["5️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"]
    ]
    return tabuleiroVisual

#Tabuleiro 10x10
def modoDificil():
    tabuleiro=[
        ["🟦", "1️⃣ ","2️⃣ ","3️⃣ ","4️⃣ ","5️⃣ ","6️⃣ ","7️⃣ ","8️⃣ ","9️⃣ ","🔟"],
        ["1️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["2️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["3️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["4️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["5️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["6️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["7️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["8️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["9️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["🔟", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"]
    ]
    return tabuleiro

    tabuleiroInimigo=[
        ["🟦", "1️⃣ ","2️⃣ ","3️⃣ ","4️⃣ ","5️⃣ ","6️⃣ ","7️⃣ ","8️⃣ ","9️⃣ ","🔟"],
        ["1️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["2️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["3️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["4️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["5️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["6️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["7️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["8️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["9️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["🔟", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"]
    ]
    return tabuleiroInimigo

    tabuleiroVisual=[
        ["🟦", "1️⃣ ","2️⃣ ","3️⃣ ","4️⃣ ","5️⃣ ","6️⃣ ","7️⃣ ","8️⃣ ","9️⃣ ","🔟"],
        ["1️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["2️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["3️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["4️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["5️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["6️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["7️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["8️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["9️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["🔟", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"]
    ]
    return tabuleiroVisual

#Impressão do tabuleiro
def imprimir(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(linha))

#Créditos
def creditos():
    os.system('cls')
    print("██████╗  █████╗ ████████╗ █████╗ ██╗     ██╗  ██╗ █████╗     ███╗   ██╗ █████╗ ██╗   ██╗ █████╗ ██╗")
    time.sleep(0.5)
    print("██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██║     ██║  ██║██╔══██╗    ████╗  ██║██╔══██╗██║   ██║██╔══██╗██║")    
    time.sleep(0.5)     
    print("██████╔╝███████║   ██║   ███████║██║     ███████║███████║    ██╔██╗ ██║███████║██║   ██║███████║██║")    
    time.sleep(0.5)     
    print("██╔══██╗██╔══██║   ██║   ██╔══██║██║     ██╔══██║██╔══██║    ██║╚██╗██║██╔══██║╚██╗ ██╔╝██╔══██║██║")    
    time.sleep(0.5)     
    print("██████╔╝██║  ██║   ██║   ██║  ██║███████╗██║  ██║██║  ██║    ██║ ╚████║██║  ██║ ╚████╔╝ ██║  ██║███████╗") 
    time.sleep(0.5)   
    print("╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═══╝╚═╝  ╚═╝  ╚═══╝  ╚═╝  ╚═╝╚══════╝") 
    time.sleep(0.5)  
                                                                                                            
    print()
    narracao("Um jogo feito por:")
    narracao("Felipe Augusto")
    narracao("Daniel Bretzke")
    narracao("Samuel Cardoso")

#Colocar embarcação
def colocarEmbarcacao(tabuleiro):

    os.system('cls')
    print("--- TABULEIRO INICIAL ---")

    imprimir(tabuleiro)

    #Define o range de acordo com o tabuleiro
    maxLinhas = len(tabuleiro) - 1
    maxColunas = len(tabuleiro[0]) - 1

    #Colocar 5 barcos
    for embarcacao in range(5):
        while True:

            linhaBarco=int(input("Qual linha deseja colocar um barco? "))
            colunaBarco=int(input("E a coluna? "))
            os.system('cls')

            #Fallback para não colocar nos números de localização
            if linhaBarco == 0 or colunaBarco == 0:
                for linha in tabuleiro:
                    print(" ".join(linha))
                print("\n Alerta do Radar: Coordenada inválida! Escolha outra.")
                continue

            #Dentro do tabuleiro
            if 1 <= linhaBarco <= maxLinhas and 1 <= colunaBarco <= maxColunas:

                #Caso ja tenha um barco
                if tabuleiro[linhaBarco][colunaBarco] == "🛥️ ":
                    print("\n Alerta do Radar: Já existe um navio nessa coordenada! Escolha outra.")
        
                #Caso não tenha
                else:
                    tabuleiro[linhaBarco][colunaBarco] = "🛥️ "

                    os.system('cls')
                    for linha in tabuleiro:
                        print(" ".join(linha))
                    print("⚓ Barco posicionado com sucesso!") 
                    time.sleep(1)

                    break  
  
            else:
                os.system('cls')
                for linha in tabuleiro:
                        print(" ".join(linha))
                print("Invalido")
            
        #Print do tabuleiro com a embarcação
        os.system('cls')
        for linha in tabuleiro:
            print(" ".join(linha))

#def atirar():

#Campanha (menu)   
def campanha():
    for i in range(1,4):
        time.sleep(0.5)
        os.system('cls')
        print("\033[47m\033[30m1- Iniciar Campanha\033[0m\n2- Como jogar\n3- Creditos\n4- Sair")
        time.sleep(0.5)
        os.system('cls')
        print("\033[40m\033[37m1- Iniciar Campanha\033[0m\n2- Como jogar\n3- Creditos\n4- Sair")

    #Ver intrudução?
    escolha = ""
    while escolha not in ("s","n"):
        os.system('cls')
        escolha = input(
            "---------------------------\n"
            "|  Ver Introduçâo?  (s/n) |\n"
            "---------------------------\n"
        ).lower()
        #Ver introdução
        if escolha == "n":
            os.system('cls')
            intro = 0
            break
        #Pular introdução
        elif escolha == "s":
            os.system('cls')
            intro = 1

            os.system('cls')
            introducao()
        else:
            os.system('cls')
            print("Comando Incorreto!")
            time.sleep(1.5)

    #Escolha da dificuldade
    escolha = ""
    while escolha not in ("facil","dificil"):
        os.system('cls')
        escolha = input(
            "--------------------------------\n"
            "|     Escolha a Modalidade     |\n"
            "--------------------------------\n"
            "-- Facil   -- Tabuleiro 5 x 10 -\n"
            "-- Dificil -- Tabuleiro 10 x 10 -\n"
        ).lower()
        #Modo fácil
        if escolha == "facil":
            modo = 1
            tabuleiro=modoFacil()
            tabuleiroInimigo=modoFacil()
            tabuleiroVisual=modoFacil()
        #Modo Dificil
        elif escolha == "dificil":
            modo = 2
            tabuleiro=modoDificil()
            tabuleiroInimigo=modoDificil()
            tabuleiroVisual=modoDificil()
        else:
            os.system('cls')
            print("Comando Incorreto!")
            time.sleep(1.5)
    
    colocarEmbarcacao(tabuleiro)

#Como jogar (menu)
def comoJogar():
    for i in range(1,2):
        time.sleep(0.5)
        os.system('cls')
        print("1- Iniciar Campanha\n\033[47m\033[30m2- Como jogar\033[0m\n3- Creditos\n4- Sair")
        time.sleep(0.5)
        os.system('cls')
        print("1- Iniciar Campanha\n\033[40m\033[37m2- Como jogar\033[0m\n3- Creditos\n4- Sair")      

#Créditos (menu)    
def creditos():
    for i in range(1,4):
        time.sleep(0.5)
        os.system('cls')
        print("1- Iniciar Campanha\n2- Como jogar\n\033[47m\033[30m3- Creditos\033[0m\n4- Sair")
        time.sleep(0.5)
        os.system('cls')
        print("1- Iniciar Campanha\n2- Como jogar\n\033[40m\033[37m3- Creditos\033[0m\n4- Sair")

    os.system('cls')
    print("██████╗  █████╗ ████████╗ █████╗ ██╗     ██╗  ██╗ █████╗     ███╗   ██╗ █████╗ ██╗   ██╗ █████╗ ██╗")
    time.sleep(0.5)
    print("██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██║     ██║  ██║██╔══██╗    ████╗  ██║██╔══██╗██║   ██║██╔══██╗██║")    
    time.sleep(0.5)     
    print("██████╔╝███████║   ██║   ███████║██║     ███████║███████║    ██╔██╗ ██║███████║██║   ██║███████║██║")    
    time.sleep(0.5)     
    print("██╔══██╗██╔══██║   ██║   ██╔══██║██║     ██╔══██║██╔══██║    ██║╚██╗██║██╔══██║╚██╗ ██╔╝██╔══██║██║")    
    time.sleep(0.5)     
    print("██████╔╝██║  ██║   ██║   ██║  ██║███████╗██║  ██║██║  ██║    ██║ ╚████║██║  ██║ ╚████╔╝ ██║  ██║███████╗") 
    time.sleep(0.5)   
    print("╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═══╝╚═╝  ╚═╝  ╚═══╝  ╚═╝  ╚═╝╚══════╝") 
    time.sleep(0.5)  
                                                                                                            
    print()
    narracao("Um jogo feito por:")
    narracao("Felipe Augusto")
    narracao("Daniel Bretzke")
    narracao("Samuel Cardoso")

#Sair
def sair():
    os.system('cls')
    print("1- Iniciar Campanha\n2- Como jogar\n3- Creditos\n\033[40m\033[37m4- Sair\033[0m")
    for i in range(1,4):
        time.sleep(0.5)
        os.system('cls')
        print("1- Iniciar Campanha\n2- Como jogar\n3- Creditos\n\033[47m\033[30m4- Sair\033[0m")
        time.sleep(0.5)
        os.system('cls')
        print("1- Iniciar Campanha\n2- Como jogar\n3- Creditos\n\033[40m\033[37m4- Sair\033[0m")

#Menu
def menu():
    while True:
        os.system('cls')

        #Fallback + Opções
        opcaoMenu = ""
        while opcaoMenu not in ("1", "2", "3", "4"):
            os.system('cls')

            print("1- Iniciar Campanha")
            print("2- Como jogar")
            print("3- Creditos")
            print("4- Sair")

            opcaoMenu = input()

        #Iniciar Campanha
        if opcaoMenu == "1":
            campanha()

            #Voltar ao menu
            while continuar != voltar or continuar != encerrar:
                continuar=input(narracao("Deseja voltar ao menu ou encerrar o jogo?")).lower()
                
                if continuar == "voltar":
                    continue

                if continuar == "encerrar":
                    break

        #Como Jogar
        elif opcaoMenu == "2":
            comoJogar()
            time.sleep(5)
            continue

        #Créditos
        elif opcaoMenu == "3":
            creditos()
            time.sleep(2)
            print()
            narracao("Voltando...",0.5)
            continue

        #Sair
        elif opcaoMenu == "4":
            sair()
            print()
            print("--Jogo encerrado.")
            break
        
#Main
def __main__():
    menu()
 
__main__()

