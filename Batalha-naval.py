import time
import sys
import random
import os

#Cores
FUNDO_BRANCO = "\033[47m"
PRETO = "\033[30m"
VERDE = "\033[92m"
RESET = "\033[0m"

#Tempo da narração (introdução)
def narracao(texto, atraso=0.07):
    sys.stdout.write(VERDE)
    sys.stdout.flush()
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(atraso)
    sys.stdout.write(RESET)
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
    print(f"{VERDE}======================================{RESET}")
    for linha in tabuleiro:
        time.sleep(0.1)
        print(f"{VERDE}||{RESET} " + " ".join(linha) + f" {VERDE}||{RESET}")
    time.sleep(0.1)
    print(f"{VERDE}======================================{RESET}")

#Colocar embarcação
def colocarEmbarcacao(tabuleiro):

    os.system('cls')
    print(f"{VERDE}======================================{RESET}")
    time.sleep(0.05)
    print(f"{VERDE}||       COLOQUE SEUS BARCOS        ||{RESET}")
    time.sleep(0.05)

    imprimir(tabuleiro)

    #Define o range de acordo com o tabuleiro
    maxLinhas = len(tabuleiro) - 1
    maxColunas = len(tabuleiro[0]) - 1

    #Colocar 5 barcos
    for embarcacao in range(5):
        while True:
            print(f"{VERDE}Qual linha deseja colocar um barco? ")
            linhaBarco = input()
            print(f"{VERDE}Qual coluna deseja colocar um barco? ")
            colunaBarco = input()
            os.system('cls')

            valido = True
            for letra in linhaBarco:
                if letra not in "1234567890":
                    valido = False
            for letra in colunaBarco:
                if letra not in "1234567890":
                    valido = False

            if not valido or linhaBarco == "" or colunaBarco == "":
                os.system('cls')
                imprimir(tabuleiro)
                narracao("\n Alerta do Radar: Coordenada inválida! Escolha outra.")
                time.sleep(1)
                continue

            # Transforma os strings em ints depois de verificar
            linhaBarco = int(linhaBarco)
            colunaBarco = int(colunaBarco)

            #Dentro do tabuleiro
            if 1 <= linhaBarco <= maxLinhas and 1 <= colunaBarco <= maxColunas:

                #Caso ja tenha um barco
                if tabuleiro[linhaBarco][colunaBarco] == "🛥️ ":

                    os.system('cls')
                    print(f"{VERDE}======================================{RESET}")
                    print(f"{VERDE}||       COLOQUE SEUS BARCOS        ||{RESET}")
                    imprimir(tabuleiro)
                    narracao("\n Alerta do Radar: Já existe um navio nessa coordenada! Escolha outra.")
                    time.sleep(1)

                    continue
        
                #Caso não tenha
                else:

                    tabuleiro[linhaBarco][colunaBarco] = "🛥️ "

                    os.system('cls')
                    print(f"{VERDE}======================================{RESET}")
                    print(f"{VERDE}||       COLOQUE SEUS BARCOS        ||{RESET}")
                    imprimir(tabuleiro)
                    print(f"{VERDE}⚓ Barco posicionado com sucesso!{RESET}") 
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

def combate(tabuleiroInimigo,tabuleiroVisual,tabuleiro,tabuleiroVisual2):

    maxLinhas = len(tabuleiroInimigo) - 1
    maxColunas = len(tabuleiroInimigo[0]) - 1
    barcos = 5
    barcosInimigos = 5

    os.system('cls')
    narracao("hora de atacar...")
    time.sleep(2)
    
    while barcosInimigos > 0 or barcos > 0: 
        while True:
            os.system('cls')
            print(f"{VERDE}======================================{RESET}")
            print(f"{VERDE}||          VISOR DO RADAR          ||{RESET}")
            imprimir(tabuleiroInimigo)
            narracao(f"\n ALVOS RESTANTES: {barcos}")
            print(f"{VERDE}Qual linha deseja atirar?{RESET}")
            linhaTiro = input()

            #Codigo Secreto
            if linhaTiro.strip().lower() == "debugmaster":
                os.system('cls')
                print(f"{VERDE}===================================================={RESET}")
                print(f"{VERDE}🏆 VITÓRIA! TODA A FROTA INIMIGA FOI DESTRUÍDA! 🏆{RESET}")
                print(f"{VERDE}===================================================={RESET}\n")
                time.sleep(3)
                return
            
            print(f"{VERDE}Qual coluna deseja atirar?{RESET}")
            colunaTiro = input()
            os.system('cls')
        
            #Fallback para não atirar nos números de localização
            valido = True
            for letra in linhaTiro:
                if letra not in "1234567890":
                    valido = False
            for letra in colunaTiro:
                if letra not in "1234567890":
                    valido = False

            if not valido or linhaTiro == "" or colunaTiro == "":
                os.system('cls')
                print(f"{VERDE}======================================{RESET}")
                print(f"{VERDE}||          VISOR DO RADAR          ||{RESET}")
                imprimir(tabuleiroInimigo)
                narracao("\n Alerta do Radar: Coordenada inválida! Escolha outra.")
                time.sleep(1)
                continue

            # Transforma os strings em ints depois de verificar
            linhaTiro = int(linhaTiro)
            colunaTiro = int(colunaTiro)

            #Dentro do tabuleiro
            if 1 <= linhaTiro <= maxLinhas and 1 <= colunaTiro <= maxColunas:

                #Caso tenha um barco
                if tabuleiroInimigo[linhaTiro][colunaTiro] == "🛥️ ":
                    tabuleiroVisual[linhaTiro][colunaTiro] = "💥"

                    os.system('cls')   
                    print(f"{VERDE}======================================{RESET}")
                    print(f"{VERDE}||          VISOR DO RADAR          ||{RESET}")
                    imprimir(tabuleiroInimigo)
                    barcosInimigos -= 1
                    narracao("\n💥 Alerta do Radar: Você acertou um barco.")
                    time.sleep(1)

                    break
        
                #Caso já tenha sido atirada
                if tabuleiroInimigo[linhaTiro][colunaTiro] == "💥" or tabuleiroInimigo[linhaTiro][colunaTiro] == "❌":

                    os.system('cls')
                    print(f"{VERDE}======================================{RESET}")
                    print(f"{VERDE}||          VISOR DO RADAR          ||{RESET}")
                    imprimir(tabuleiroInimigo)
                    narracao("\n Alerta do Radar: Esta cordenada já foi atirada! Escolha outra.")
                    time.sleep(1)

                    continue

                #Caso não tenha nada
                else:

                    tabuleiroInimigo[linhaTiro][colunaTiro] = "❌"
                    os.system('cls')
                    print(f"{VERDE}======================================{RESET}")
                    print(f"{VERDE}||          VISOR DO RADAR          ||{RESET}")
                    imprimir(tabuleiroInimigo)
                    narracao("\n❌ Não havia nada nesta coordenada, apenas água...") 
                    time.sleep(1)

                    break  

            else:

                os.system('cls')
                print(f"{VERDE}======================================{RESET}")
                print(f"{VERDE}||          VISOR DO RADAR          ||{RESET}")
                imprimir(tabuleiroInimigo)
                narracao("\n Inválido")
                time.sleep(2)
                continue

        #Vez do Inimigo
        while True:

            maxLinhas = len(tabuleiro) - 1
            maxColunas = len(tabuleiro[0]) - 1
            
            i = random.randint(1,maxLinhas)
            j = random.randint(1,maxColunas)

            narracao("O inimigo está preparando para atacar...")
            time.sleep(2)

            #Caso tenha um barco
            if tabuleiro[i][j] == "🛥️ ":
                tabuleiro[i][j] = "💥 "

                os.system('cls')
                print(f"{VERDE}======================================{RESET}")
                print(f"{VERDE}||         ATAQUES INIMIGOS         ||{RESET}")   
                imprimir(tabuleiro)

                barcos -= 1
                narracao("\n💥 Alerta do Radar: O inimigo acertou uma de suas embarcações.")
                time.sleep(1)
                break
    
            #Caso já tenha sido atirada
            if tabuleiro[i][j] == "💥 " or tabuleiroVisual2[i][j] == "❌":

                continue

            #Caso não tenha nada
            else:
                tabuleiro[i][j] = "❌"
                os.system('cls')
                print(f"{VERDE}======================================{RESET}")
                print(f"{VERDE}||         ATAQUES INIMIGOS         ||{RESET}")
                imprimir(tabuleiro)
                narracao("\n❌ O inimigo errou, não havia nada nesta coordenada, apenas água...") 
                time.sleep(1)

                break 

    #Mensagem de vitória
    time.sleep(2)
    os.system('cls')
    print(f"{VERDE}===================================================={RESET}")
    print(f"{VERDE}🏆 VITÓRIA! TODA A FROTA INIMIGA FOI DESTRUÍDA! 🏆{RESET}")
    print(f"{VERDE}===================================================={RESET}\n")
    time.sleep(3)

#Campanha (menu)   
def campanha():
    for i in range(1,4):
        time.sleep(0.5)
        os.system('cls')
        print(f"{VERDE}=============================================={RESET}")
        print(f"{VERDE}||                                          ||{RESET}")
        print(f"{VERDE}||         1 -   {FUNDO_BRANCO}{PRETO}Iniciar Campanha{RESET}{VERDE}           ||{RESET}")
        print(f"{VERDE}||                                          ||{RESET}")
        print(f"{VERDE}||         2 -     Como Jogar               ||{RESET}")
        print(f"{VERDE}||                                          ||{RESET}")
        print(f"{VERDE}||         3 -      Créditos                ||{RESET}")
        print(f"{VERDE}||                                          ||{RESET}")
        print(f"{VERDE}||         4 -     Fechar Jogo              ||{RESET}")
        print(f"{VERDE}||                                          ||{RESET}")
        print(f"{VERDE}=============================================={RESET}")
        time.sleep(0.5)
        os.system('cls')
        print(f"{VERDE}=============================================={RESET}")
        print(f"{VERDE}||                                          ||{RESET}")
        print(f"{VERDE}||         1 -   Iniciar Campanha           ||{RESET}")
        print(f"{VERDE}||                                          ||{RESET}")
        print(f"{VERDE}||         2 -     Como Jogar               ||{RESET}")
        print(f"{VERDE}||                                          ||{RESET}")
        print(f"{VERDE}||         3 -      Créditos                ||{RESET}")
        print(f"{VERDE}||                                          ||{RESET}")
        print(f"{VERDE}||         4 -     Fechar Jogo              ||{RESET}")
        print(f"{VERDE}||                                          ||{RESET}")
        print(f"{VERDE}=============================================={RESET}")

    #Ver intrudução?
    escolha = ""
    while escolha not in ("s","n"):

        os.system('cls')
        
        print(f"{VERDE}=============================================={RESET}")
        time.sleep(0.1)
        print(f"{VERDE}||                                          ||{RESET}")
        time.sleep(0.1)
        print(f"{VERDE}||           Gostaria de Assistir           ||{RESET}")
        time.sleep(0.1)
        print(f"{VERDE}||              a Introdução?               ||{RESET}")
        time.sleep(0.1)
        print(f"{VERDE}||                                          ||{RESET}")
        time.sleep(0.1)
        print(f"{VERDE}==================( s / n )==================={RESET}")
        
        escolha = input().lower()

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
        print(f"{VERDE}=============================================={RESET}")
        time.sleep(0.1)
        print(f"{VERDE}||                                          ||{RESET}")
        time.sleep(0.1)
        print(f"{VERDE}||           Escolha a Modalidade           ||{RESET}")
        time.sleep(0.1)
        print(f"{VERDE}||                                          ||{RESET}")
        time.sleep(0.1)
        print(f"{VERDE}=============================================={RESET}")
        time.sleep(0.1)
        print(f"{VERDE}||                                          ||{RESET}")
        time.sleep(0.1)
        print(f"{VERDE}||      Facil      --   Tabuleiro 5 x 10    ||{RESET}")
        time.sleep(0.1)
        print(f"{VERDE}||      Dificil    --   Tabuleiro 10 x 10   ||{RESET}")
        time.sleep(0.1)
        print(f"{VERDE}||                                          ||{RESET}")
        time.sleep(0.1)
        print(f"{VERDE}=============( Facil / Dificil )=============={RESET}")
        escolha = input().lower()

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

    combate(tabuleiroInimigo, tabuleiroVisual, tabuleiro, tabuleiroVisual2)

#Como jogar (menu)
def comoJogar():
    for i in range(1,4):
        time.sleep(0.5)
        os.system('cls')
        print(f"{VERDE}=============================================={RESET}")
        print(f"{VERDE}||                                          ||{RESET}")
        print(f"{VERDE}||         1 -   Iniciar Campanha           ||{RESET}")
        print(f"{VERDE}||                                          ||{RESET}")
        print(f"{VERDE}||         2 -     {FUNDO_BRANCO}{PRETO}Como Jogar{RESET}{VERDE}               ||{RESET}")
        print(f"{VERDE}||                                          ||{RESET}")
        print(f"{VERDE}||         3 -      Créditos                ||{RESET}")
        print(f"{VERDE}||                                          ||{RESET}")
        print(f"{VERDE}||         4 -     Fechar Jogo              ||{RESET}")
        print(f"{VERDE}||                                          ||{RESET}")
        print(f"{VERDE}=============================================={RESET}")
        time.sleep(0.5)
        os.system('cls')
        print(f"{VERDE}=============================================={RESET}")
        print(f"{VERDE}||                                          ||{RESET}")
        print(f"{VERDE}||         1 -   Iniciar Campanha           ||{RESET}")
        print(f"{VERDE}||                                          ||{RESET}")
        print(f"{VERDE}||         2 -     Como Jogar               ||{RESET}")
        print(f"{VERDE}||                                          ||{RESET}")
        print(f"{VERDE}||         3 -      Créditos                ||{RESET}")
        print(f"{VERDE}||                                          ||{RESET}")
        print(f"{VERDE}||         4 -     Fechar Jogo              ||{RESET}")
        print(f"{VERDE}||                                          ||{RESET}")
        print(f"{VERDE}=============================================={RESET}")

    os.system("cls")

    print(f"{VERDE} COMO JOGAR {RESET}")
    

    print(f"{VERDE}======================{RESET}")
    print(f"{VERDE}||  {RESET}🌊 🌊 🌊 🌊 🌊{VERDE}  ||{RESET}")
    print(f"{VERDE}||  {RESET}🌊 🚢 🚢 🚢 🌊{VERDE}  ||{RESET}")
    print(f"{VERDE}||  {RESET}🌊 🌊 🌊 🌊 🌊{VERDE}  ||{RESET}")
    print(f"{VERDE}||  {RESET}🌊 🌊 🌊 🌊 🌊{VERDE}  ||{RESET}")
    print(f"{VERDE}||  {RESET}🌊 🌊 🌊 🌊 🌊{VERDE}  ||{RESET}")
    print(f"{VERDE}======================{RESET}")

    time.sleep(1.2)
    print()
    narracao("🚢 = Navio")
    narracao("🌊 = Água")
    narracao("Os navios ficam escondidos no tabuleiro.")
    print()
    
    input(f"{VERDE}Pressione ENTER para continuar: {RESET}")

    os.system("cls")

    print(f"{VERDE} COMO JOGAR {RESET}")

    print(f"{VERDE}======================{RESET}")
    print(f"{VERDE}||  {RESET}🌊 🌊 🌊 🌊 🌊{VERDE}  ||{RESET}")
    print(f"{VERDE}||  {RESET}🌊 💥 🚢 🚢 🌊{VERDE}  ||{RESET}")
    print(f"{VERDE}||  {RESET}🌊 🌊 🌊 🌊 🌊{VERDE}  ||{RESET}")
    print(f"{VERDE}||  {RESET}🌊 🌊 🌊 🌊 🌊{VERDE}  ||{RESET}")
    print(f"{VERDE}||  {RESET}🌊 🌊 🌊 🌊 🌊{VERDE}  ||{RESET}")
    print(f"{VERDE}======================{RESET}")

    print()
    narracao("💥 = Você acertou!")
    narracao("Quando você atinge um navio, a posição é marcada com 💥.")

    input(f"{VERDE}Pressione ENTER para continuar: {RESET}")

    os.system('cls')

    print(f"{VERDE} COMO JOGAR {RESET}")

    print(f"{VERDE}======================{RESET}")
    print(f"{VERDE}||  {RESET}🌊 🌊 🌊 🌊 🌊{VERDE}  ||{RESET}")
    print(f"{VERDE}||  {RESET}🌊 ❌ 🚢 🚢 🌊{VERDE}  ||{RESET}")
    print(f"{VERDE}||  {RESET}🌊 🌊 🌊 🌊 🌊{VERDE}  ||{RESET}")
    print(f"{VERDE}||  {RESET}🌊 🌊 🌊 🌊 🌊{VERDE}  ||{RESET}")
    print(f"{VERDE}||  {RESET}🌊 🌊 🌊 🌊 🌊{VERDE}  ||{RESET}")
    print(f"{VERDE}======================{RESET}")

    print()
    narracao("❌ = Você errou o disparo...")
    narracao("Se não houver um navio na coordenada escolhida, você erra o disparo.")

    print()
    input(f"{VERDE}Pressione ENTER para continuar: {RESET}")

    os.system("cls")

    print(f"{VERDE} OBJETIVO {RESET}")

    print()
    narracao("🎯 Afundar todos os navios inimigos.")
    narracao("🚢 Cada navio ocupa uma posição.")
    narracao("💥 Ao todo são cinco navios.")
    narracao("🏆 Destrua toda a frota para vencer a batalha!")

    input(f"{VERDE}Pressione ENTER para voltar ao menu: {RESET}")


#Créditos (menu)    
def creditos():
    for i in range(1,4):
        time.sleep(0.5)
        os.system('cls')
        print(f"{VERDE}=============================================={RESET}")
        print(f"{VERDE}||                                          ||{RESET}")
        print(f"{VERDE}||         1 -   Iniciar Campanha           ||{RESET}")
        print(f"{VERDE}||                                          ||{RESET}")
        print(f"{VERDE}||         2 -     Como Jogar               ||{RESET}")
        print(f"{VERDE}||                                          ||{RESET}")
        print(f"{VERDE}||         3 -      {FUNDO_BRANCO}{PRETO}Créditos{RESET}{VERDE}                ||{RESET}")
        print(f"{VERDE}||                                          ||{RESET}")
        print(f"{VERDE}||         4 -     Fechar Jogo              ||{RESET}")
        print(f"{VERDE}||                                          ||{RESET}")
        print(f"{VERDE}=============================================={RESET}")
        time.sleep(0.5)
        os.system('cls')
        print(f"{VERDE}=============================================={RESET}")
        print(f"{VERDE}||                                          ||{RESET}")
        print(f"{VERDE}||         1 -   Iniciar Campanha           ||{RESET}")
        print(f"{VERDE}||                                          ||{RESET}")
        print(f"{VERDE}||         2 -     Como Jogar               ||{RESET}")
        print(f"{VERDE}||                                          ||{RESET}")
        print(f"{VERDE}||         3 -      Créditos                ||{RESET}")
        print(f"{VERDE}||                                          ||{RESET}")
        print(f"{VERDE}||         4 -     Fechar Jogo              ||{RESET}")
        print(f"{VERDE}||                                          ||{RESET}")
        print(f"{VERDE}=============================================={RESET}")

    os.system('cls')
    print(f"{VERDE}██████╗  █████╗ ████████╗ █████╗ ██╗     ██╗  ██╗ █████╗     ███╗   ██╗ █████╗ ██╗   ██╗ █████╗ ██╗{RESET}")
    time.sleep(0.5)
    print(f"{VERDE}██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██║     ██║  ██║██╔══██╗    ████╗  ██║██╔══██╗██║   ██║██╔══██╗██║{RESET}")    
    time.sleep(0.5)     
    print(f"{VERDE}██████╔╝███████║   ██║   ███████║██║     ███████║███████║    ██╔██╗ ██║███████║██║   ██║███████║██║{RESET}")    
    time.sleep(0.5)     
    print(f"{VERDE}██╔══██╗██╔══██║   ██║   ██╔══██║██║     ██╔══██║██╔══██║    ██║╚██╗██║██╔══██║╚██╗ ██╔╝██╔══██║██║{RESET}")    
    time.sleep(0.5)     
    print(f"{VERDE}██████╔╝██║  ██║   ██║   ██║  ██║███████╗██║  ██║██║  ██║    ██║ ╚████║██║  ██║ ╚████╔╝ ██║  ██║███████╗{RESET}") 
    time.sleep(0.5)   
    print(f"{VERDE}╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═══╝╚═╝  ╚═╝  ╚═══╝  ╚═╝  ╚═╝╚══════╝{RESET}") 
    time.sleep(0.5)  
                                                                                                            
    print()
    narracao(f"{VERDE}Um jogo feito por:")
    narracao(f"{VERDE}Felipe Augusto")
    narracao(f"{VERDE}Daniel Bretzke")
    narracao(f"{VERDE}Samuel Cardoso")

#Sair (menu)
def sair():
    for i in range(1,4):
        time.sleep(0.5)
        os.system('cls')
        print(f"{VERDE}=============================================={RESET}")
        print(f"{VERDE}||                                          ||{RESET}")
        print(f"{VERDE}||         1 -   Iniciar Campanha           ||{RESET}")
        print(f"{VERDE}||                                          ||{RESET}")
        print(f"{VERDE}||         2 -     Como Jogar               ||{RESET}")
        print(f"{VERDE}||                                          ||{RESET}")
        print(f"{VERDE}||         3 -      Créditos                ||{RESET}")
        print(f"{VERDE}||                                          ||{RESET}")
        print(f"{VERDE}||         4 -     {FUNDO_BRANCO}{PRETO}Fechar Jogo{RESET}{VERDE}              ||{RESET}")
        print(f"{VERDE}||                                          ||{RESET}")
        print(f"{VERDE}=============================================={RESET}")
        time.sleep(0.5)
        os.system('cls')
        print(f"{VERDE}=============================================={RESET}")
        print(f"{VERDE}||                                          ||{RESET}")
        print(f"{VERDE}||         1 -   Iniciar Campanha           ||{RESET}")
        print(f"{VERDE}||                                          ||{RESET}")
        print(f"{VERDE}||         2 -     Como Jogar               ||{RESET}")
        print(f"{VERDE}||                                          ||{RESET}")
        print(f"{VERDE}||         3 -      Créditos                ||{RESET}")
        print(f"{VERDE}||                                          ||{RESET}")
        print(f"{VERDE}||         4 -     Fechar Jogo              ||{RESET}")
        print(f"{VERDE}||                                          ||{RESET}")
        print(f"{VERDE}=============================================={RESET}")

#Menu
def menu():

    while True:
        os.system('cls')

        #Fallback + Opções
        opcaoMenu = ""
        while opcaoMenu not in ("1", "2", "3", "4"):
            os.system('cls')

            print(f"{VERDE}=============================================={RESET}")
            time.sleep(0.1)
            print(f"{VERDE}||                                          ||{RESET}")
            time.sleep(0.1)
            print(f"{VERDE}||         1 -   Iniciar Campanha           ||{RESET}")
            time.sleep(0.1)
            print(f"{VERDE}||                                          ||{RESET}")
            time.sleep(0.1)
            print(f"{VERDE}||         2 -     Como Jogar               ||{RESET}")
            time.sleep(0.1)
            print(f"{VERDE}||                                          ||{RESET}")
            time.sleep(0.1)
            print(f"{VERDE}||         3 -      Créditos                ||{RESET}")
            time.sleep(0.1)
            print(f"{VERDE}||                                          ||{RESET}")
            time.sleep(0.1)
            print(f"{VERDE}||         4 -     Fechar Jogo              ||{RESET}")
            time.sleep(0.1)
            print(f"{VERDE}||                                          ||{RESET}")
            time.sleep(0.1)
            print(f"{VERDE}=============================================={RESET}")

            opcaoMenu = input()

        #Iniciar Campanha
        if opcaoMenu == "1":
            campanha()

        #Como Jogar
        elif opcaoMenu == "2":
            comoJogar()
            print()
            narracao("Voltando...",0.3)
            continue

        #Créditos
        elif opcaoMenu == "3":
            creditos()
            print()
            narracao("Voltando...",0.3)
            continue

        #Sair
        elif opcaoMenu == "4":
            sair()
            print()
            os.system('cls')
            print("--Jogo encerrado.")
            break
        
#Main
def __main__():
    menu()


__main__()
