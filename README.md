# ⚓ BATALHA NAVAL

## 📖 Sobre o Projeto

Batalha Naval é um jogo desenvolvido em Python inspirado no clássico jogo de estratégia naval. O projeto foi criado com o objetivo de aplicar conceitos fundamentais de programação, como estruturas de repetição, funções, listas bidimensionais (matrizes), condicionais e interação com o usuário através do terminal.

A proposta do jogo é colocar o jogador no papel de um comandante naval durante a Segunda Guerra Mundial. Em meio a uma densa neblina no Oceano Atlântico Sul, o sistema de radar falha e a única forma de sobreviver é utilizar estratégia e lógica para localizar e destruir a frota inimiga.

Além da mecânica principal do jogo, esta versão já conta com uma introdução narrativa para aumentar a imersão do jogador e um tutorial explicando as regras básicas da Batalha Naval.

---

## 🎯 Objetivos do Projeto

* Desenvolver um jogo utilizando a linguagem Python.
* Aplicar conceitos aprendidos em sala de aula.
* Trabalhar com matrizes para representar tabuleiros.
* Criar menus interativos.
* Utilizar funções para organizar o código.
* Desenvolver lógica de navegação entre telas.
* Implementar futuramente o sistema completo de combate naval.

---

## 🗺️ Estrutura Atual do Jogo

Atualmente o projeto possui as seguintes funcionalidades:

### ✅ Menu Principal

O menu permite ao usuário navegar pelas opções disponíveis:

```text
1 - Iniciar Campanha
2 - Como Jogar
3 - Créditos
4 - Sair
```

---

### ✅ Introdução Narrativa

Antes do início da campanha, o jogador acompanha uma pequena história ambientada em 1942.

A introdução utiliza um efeito de digitação para tornar a experiência mais dinâmica e imersiva.

Exemplo:

```text
Ano: 1942

Oceano Atlântico Sul - 03:42 da madrugada

Comandante... o radar parou de responder.
Pane geral. Estamos cegos.
```

---

### ✅ Tutorial

O tutorial apresenta as regras básicas do jogo utilizando exemplos visuais do tabuleiro.

Ele explica:

* O que representa a água.
* O que representa um navio.
* Como identificar um acerto.
* Como identificar um erro.
* O objetivo principal da partida.

---

### ✅ Modos de Dificuldade

O jogador pode escolher entre dois tamanhos de tabuleiro:

#### Fácil

```text
5 linhas x 10 colunas
```

#### Difícil

```text
10 linhas x 10 colunas
```

---

## 🧩 Estrutura das Funções

### narracao()

Responsável por exibir textos letra por letra, simulando uma narração.

---

### introducao()

Exibe toda a história inicial da campanha.

---

### tutorial()

Apresenta as regras do jogo através de exemplos visuais e retorna ao menu principal após a conclusão.

---

### modoFacil()

Cria e retorna um tabuleiro de tamanho 5x10.

---

### modoDificil()

Cria e retorna um tabuleiro de tamanho 10x10.

---

### imprimir()

Mostra o conteúdo do tabuleiro no terminal.

---

### menu()

Controla toda a navegação entre as telas do sistema.

---

## 🖥️ Representação do Tabuleiro

Exemplo de tabuleiro:

```text
🌊 🌊 🌊 🌊 🌊
🌊 🚢 🚢 🚢 🌊
🌊 🌊 🌊 🌊 🌊
🌊 🌊 🌊 🌊 🌊
🌊 🌊 🌊 🌊 🌊
```

### Legenda

| Símbolo | Significado |
| ------- | ----------- |
| 🌊      | Água        |
| 🚢      | Navio       |
| 💥      | Acerto      |
| ❌       | Erro        |

---

## 👥 Integrantes

* Samuel Cardoso
* Felipe Augusto
* Daniel Bredzke

---

## 📌 Versão Atual

**Versão 0.1**

Primeira versão funcional contendo:

* Menu principal
* Introdução narrativa
* Tutorial
* Modos de dificuldade
* Exibição de tabuleiros

Esta versão serve como base para a implementação completa da mecânica de batalha naval nas próximas etapas do projeto.
