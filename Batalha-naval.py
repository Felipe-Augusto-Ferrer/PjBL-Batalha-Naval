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

    tabuleiroInimigo=[
        ["🟦","1️⃣ ","2️⃣ ","3️⃣ ","4️⃣ ","5️⃣ ","6️⃣ ","7️⃣ ","8️⃣ ","9️⃣ ","🔟"],
        ["1️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["2️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["3️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["4️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["5️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"]
    ]

    tabuleiroVisual=[
        ["🟦","1️⃣ ","2️⃣ ","3️⃣ ","4️⃣ ","5️⃣ ","6️⃣ ","7️⃣ ","8️⃣ ","9️⃣ ","🔟"],
        ["1️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["2️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["3️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["4️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["5️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"]
    ]

    tabuleiroVisual2=[
        ["🟦","1️⃣ ","2️⃣ ","3️⃣ ","4️⃣ ","5️⃣ ","6️⃣ ","7️⃣ ","8️⃣ ","9️⃣ ","🔟"],
        ["1️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["2️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["3️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["4️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"],
        ["5️⃣ ", "🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊","🌊"]
    ]

    return tabuleiro, tabuleiroInimigo, tabuleiroVisual, tabuleiroVisual2

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

    tabuleiroVisual2=[
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

    return tabuleiro, tabuleiroInimigo, tabuleiroVisual, tabuleiroVisual2

#Impressão do tabuleiro
def imprimir(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(linha))

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

                imprimir(tabuleiro)
                narracao("\n Alerta do Radar: Coordenada inválida! Escolha outra.")

                continue

            #Dentro do tabuleiro
            if 1 <= linhaBarco <= maxLinhas and 1 <= colunaBarco <= maxColunas:

                #Caso ja tenha um barco
                if tabuleiro[linhaBarco][colunaBarco] == "🛥️ ":

                    os.system('cls')
                    imprimir(tabuleiro)
                    narracao("\n Alerta do Radar: Já existe um navio nessa coordenada! Escolha outra.")
                    time.sleep(1)

                    continue
        
                #Caso não tenha
                else:

                    tabuleiro[linhaBarco][colunaBarco] = "🛥️ "

                    os.system('cls')
                    imprimir(tabuleiro)
                    narracao("⚓ Barco posicionado com sucesso!") 
                    time.sleep(1)

                    break  
  
            else:

                os.system('cls')
                imprimir(tabuleiro)
                narracao("Invalido")
                time.sleep(1)

                continue
            
    #Print do tabuleiro com a embarcação
    os.system('cls')
    narracao("Coordenadas finais para as embarcações:")
    imprimir(tabuleiro)
    time.sleep(3)

#Colocar a ebarcação do computador
def colocarEmbarcacaoInimigo(tabuleiroInimigo):

    #Delimitação de linhas/colunas de acordo com a dificuldade
    maxLinhas = len(tabuleiroInimigo) - 1
    maxColunas = len(tabuleiroInimigo[0]) - 1

    for embarcacao in range(5):
        while True:
            i=random.randint(1,maxLinhas)
            j=random.randint(1,maxColunas)

            if tabuleiroInimigo[i][j]== "🌊":
                tabuleiroInimigo[i][j]=="🛥️ "

                break

#def tiroInimigo(tabuleiro,tabuleiroVisual2):

def combate(tabuleiroInimigo,tabuleiroVisual):

    maxLinhas = len(tabuleiroInimigo) - 1
    maxColunas = len(tabuleiroInimigo[0]) - 1
    barcos = 5
    barcosInimigos = 5

    os.system('cls')
    print("---VISOR DO RADAR---")
    imprimir(tabuleiroVisual)
    narracao(f"\n ALVOS RESTANTES: {barcos}")
    
    while barcosInimigos > 0 or barcos > 0: 
        while True:
            linhaTiro=int(input("Qual linha deseja atirar? "))
            colunaTiro=int(input("Qual coluna deseja atirar? "))
            os.system('cls')

            #Fallback para não atirar nos números de localização
            if linhaTiro <= 0 or colunaTiro <= 0:
                imprimir(tabuleiroVisual)
                narracao("\n Alerta do Radar: Coordenada inválida! Escolha outra.")

            #Dentro do tabuleiro
            if 1 <= linhaTiro <= maxLinhas and 1 <= colunaTiro <= maxColunas:

                #Caso tenha um barco
                if tabuleiroInimigo[linhaTiro][colunaTiro] == "🛥️ ":
                    tabuleiroVisual[linhaTiro][colunaTiro] = "💥 "

                    os.system('cls')   

                    imprimir(tabuleiroVisual)
                    barcosInimigos -= 1
                    narracao("\n 💥 Alerta do Radar: Você acertou um barco.")
                    time.sleep(1)

                    break
        
                #Caso já tenha sido atirada
                if tabuleiroInimigo[linhaTiro][colunaTiro] == "💥 " or tabuleiroVisual[linhaTiro][colunaTiro] == "❌ ":

                    os.system('cls')
                    imprimir(tabuleiroVisual)
                    narracao("\n Alerta do Radar: Esta cordenada já foi atirada! Escolha outra.")
                    time.sleep(1)

                    continue

                #Caso não tenha nada
                else:

                    tabuleiroInimigo[linhaTiro][colunaTiro] = "❌ "
                    os.system('cls')

                    imprimir(tabuleiroVisual)
                    narracao("\n ❌ Não havia nada nesta coordenada, apenas água...") 
                    time.sleep(1)

                    break  

            else:

                os.system('cls')
                imprimir(tabuleiroVisual)
                narracao("\n Inválido")
                time.sleep(2)
                continue

        #Vez do Inimigo
        while True:

            maxLinhas = len(tabuleiro) - 1
            maxColunas = len(tabuleiro[0]) - 1
            
            i = random.randint(1,maxlinhas)
            j = random.randint(1,maxColunas)

            narracao("O inimigo está preparando para atacar...")
            time.sleep(2)

            #Caso tenha um barco
            if tabuleiro[i][j] == "🛥️ ":
                tabuleiroVisual2[i][j] = "💥 "

                os.system('cls')   
                imprimir(tabuleiroVisual2)

                barcos -= 1
                narracao("\n 💥 Alerta do Radar: O inimigo acertou uma de suas embarcações.")
                time.sleep(1)
                break
    
            #Caso já tenha sido atirada
            if tabuleiroInimigo2[i][j] == "💥 " or tabuleiroVisual2[i][j] == "❌ ":

                continue

            #Caso não tenha nada
            else:
                tabuleiro[i][j] = "❌ "
                os.system('cls')
                imprimir(tabuleiroVisual2)
                narracao("\n ❌ O inimigo errou, não havia nada nesta coordenada, apenas água...") 
                time.sleep(1)

                break 

    #Mensagem de vitória
    time.sleep(2)
    os.system('cls')
    print("=========================================")
    print("🏆 VITÓRIA! TODA A FROTA INIMIGA FOI DESTRUÍDA! 🏆")
    print("=========================================")
    time.sleep(3)

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
            tabuleiro, tabuleiroInimigo, tabuleiroVisual, tabuleiroVisual2 = modoFacil()

        #Modo Dificil
        elif escolha == "dificil":
            tabuleiro, tabuleiroInimigo, tabuleiroVisual, tabuleiroVisual2 = modoDificil()

        else:
            os.system('cls')
            print("Comando Incorreto!")
            time.sleep(1.5)
    
    colocarEmbarcacao(tabuleiro)

    colocarEmbarcacaoInimigo(tabuleiroInimigo)

    combate(tabuleiroInimigo, tabuleiroVisual)

#Como jogar (menu)
def comoJogar():
    for i in range(1,4):
        time.sleep(0.5)
        os.system('cls')
        print("1- Iniciar Campanha\n\033[47m\033[30m2- Como jogar\033[0m\n3- Creditos\n4- Sair")
        time.sleep(0.5)
        os.system('cls')
        print("1- Iniciar Campanha\n\033[40m\033[37m2- Como jogar\033[0m\n3- Creditos\n4- Sair")      

    os.system("cls")

    print(" COMO JOGAR ")

    print("    A B C D E")
    print("1   🌊 🌊 🌊 🌊 🌊")
    print("2   🌊 🚢 🚢 🚢 🌊")
    print("3   🌊 🌊 🌊 🌊 🌊")
    print("4   🌊 🌊 🌊 🌊 🌊")
    print("5   🌊 🌊 🌊 🌊 🌊")

    time.sleep(1.2)
    print()
    narracao("🚢 = Navio")
    narracao("🌊 = Água")
    narracao("Os navios ficam escondidos no tabuleiro.")
    print()
    continuar = input("Digite 1 para continuar: ")

    while continuar != "1":
        continuar = input("Digite 1 para continuar: ")

    os.system("cls")

    print(" COMO JOGAR ")

    print("    A B C D E")
    print("1   🌊 🌊 🌊 🌊 🌊")
    print("2   🌊 💥 🚢 🚢 🌊")
    print("3   🌊 🌊 🌊 🌊 🌊")
    print("4   🌊 🌊 🌊 🌊 🌊")
    print("5   🌊 🌊 🌊 🌊 🌊")

    print()
    narracao("💥 = Você acertou!")
    narracao("Quando você atinge um navio, a posição é marcada com 💥.")
    continuar = input("Digite 1 para continuar: ")

    while continuar != "1":
        continuar = input("Digite 1 para continuar: ")

    os.system('cls')

    print(" COMO JOGAR ")

    print("    A B C D E")
    print("1   🌊 🌊 🌊 🌊 🌊")
    print("2   🌊 ❌ 🌊 🌊 🌊")
    print("3   🌊 🌊 🌊 🌊 🌊")
    print("4   🌊 🌊 🌊 🌊 🌊")
    print("5   🌊 🌊 🌊 🌊 🌊")

    print()
    narracao("❌ = Você errou o disparo...")
    narracao("Se não houver um navio na coordenada escolhida, você erra o disparo.")

    print()
    continuar = input("Digite 1 para continuar: ")

    while continuar != "1":
        continuar = input("Digite 1 para continuar: ")

    os.system("cls")

    print(" OBJETIVO ")

    print()
    narracao("🎯 Afundar todos os navios inimigos.")
    narracao("🚢 Cada navio ocupa uma posição.")
    narracao("💥 Ao todo são cinco navios.")
    narracao("🏆 Destrua toda a frota para vencer a batalha!")

    continuarmenu = input("Digite 1 para voltar ao menu: ")

    while continuarmenu != "1":
        continuarmenu = input("Digite 1 para voltar ao menu: ")

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

#Sair (menu)
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
            continuar = ""
            while continuar != "s" and continuar != "n":
                continuar=input(narracao("Deseja voltar ao menu?(s/n)")).lower()
                
                if continuar == "s":
                    continue

                elif continuar == "n":
                    break

                else:
                    print("Incorreto, digite 's' ou 'n':")

        #Como Jogar
        elif opcaoMenu == "2":
            comoJogar()
            print()
            narracao("Voltando...",0.7)
            continue

        #Créditos
        elif opcaoMenu == "3":
            creditos()
            print()
            narracao("Voltando...",0.7)
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

