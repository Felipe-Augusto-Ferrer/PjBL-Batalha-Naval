import time
import sys
import random
import os

#Tempo da narração
def narracao(texto, atraso=0.07):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(atraso)
    print()

#Introdução pra companha do jogo (a mudar):
def introducao():
    print()
    narracao("BATALHA NAVAL")
    print()
    time.sleep(1.2)

    narracao("Ano: 1942")
    time.sleep(1.2)
    narracao("Oceano Atlântico Sul - 03:42 da madrugada")
    time.sleep(1.5)

    print()
    narracao("*O som das ondas colidindo contra o casco de aço é a única coisa real.*")
    narracao("*Lá fora, uma névoa espessa e escura engoliu o horizonte.*")
    narracao("*Você não enxerga a proa do seu próprio navio.*")
    time.sleep(1.2)

    print()
    narracao("*Na sala de comando, as luzes brancas foram apagadas.*")
    narracao("*Resta apenas o brilho vermelho e estático dos painéis de emergência.*")
    narracao("*O operador do radar se vira para você. O rosto dele está pálido.*")
    time.sleep(1.5)
    print()
    narracao("-Comandante... o radar parou de responder. Pane geral. Estamos cegos.")
    time.sleep(1.5)

    print()
    narracao("*Você caminha até a mesa tática. O silêncio na sala é sufocante.*")
    narracao("*Você sabe que, em algum lugar desse quadrante escuro, ELES estão caçando você.*")
    narracao("*Porta-aviões, cruzadores, submarinos... fantasmas de metal escondidos no nevoeiro.*")
    time.sleep(1.2)

    print()
    narracao("*Se você se mover, revelará sua posição.*")
    narracao("*Se ficar parado, será um alvo fácil.*")
    time.sleep(1.2)

    print()
    narracao("*O oficial de armas destrava o painel de artilharia pesada.*")
    narracao("*Os canhões estão carregados. O metal range com a pressão hidráulica.*")
    time.sleep(1.2)
    
    print()
    narracao("*Todos os olhos da sala de comando se voltam para você.*")
    narracao("*Eles esperam sua ordem. Sua mente é a única arma que restou.*")
    time.sleep(1.5)

    print()
    narracao("-Prontos para disparar, Senhor. Diga-nos para onde apontar...")
    time.sleep(1.2)

    print()
    narracao("...",1.5)
    time.sleep(2.0)

    print()
    narracao("---SUA MISSÃO: Deduzir as coordenadas e estraçalhar a frota inimiga.")
    narracao("               Um erro... e o seu navio será o próximo a afundar.")
    
    time.sleep(1.0)
    print()
    print()
    narracao("Você está pronto?")
    print()
    print("=" * 70 + "\n")
    time.sleep(1.0)
introducao()
