
# ==========================================
# TRABALHO FABIO - ESTRUTURAS DE DADOS
# PILHA, FILA, FILA CIRCULAR E ORDENACAO
# ==========================================

# Variaveis principais
dados = []
tamanho = 0
estrutura = None

# Variaveis utilizadas na fila circular
inicio = 0
fim = 0
quantidade = 0


# ==========================================
# FUNCAO PARA LER NUMEROS INTEIROS
# ==========================================

def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite apenas numeros inteiros!")


# ==========================================
# CRIAR ESTRUTURA
# ==========================================

def criar_estrutura(tipo):
    global dados, tamanho, estrutura
    global inicio, fim, quantidade

    capacidade = ler_inteiro("Digite o tamanho da estrutura: ")

    if capacidade <= 0:
        print("O tamanho deve ser maior que zero!")
        return

    tamanho = capacidade
    estrutura = tipo

    inicio = 0
    fim = 0
    quantidade = 0

    if tipo == "FILA CIRCULAR":
        dados = [None] * tamanho
    else:
        dados = []

    print(tipo, "criada com sucesso!")


# ==========================================
# ARMAZENAR VALOR - PUSH / ENQUEUE
# ==========================================

def armazenar_valor():
    global fim, quantidade

    if estrutura is None:
        print("Crie uma estrutura primeiro!")
        return

    if quantidade >= tamanho:
        print("Estrutura cheia!")
        return

    valor = ler_inteiro("Digite o valor que deseja armazenar: ")

    if estrutura == "FILA CIRCULAR":
        dados[fim] = valor
        fim = (fim + 1) % tamanho
        quantidade += 1

    else:
        dados.append(valor)
        quantidade += 1

    print("Valor armazenado com sucesso!")


# ==========================================
# EXTRAIR VALOR - POP / DEQUEUE
# ==========================================

def extrair_valor():
    global inicio, quantidade

    if estrutura is None:
        print("Crie uma estrutura primeiro!")
        return

    if quantidade == 0:
        print("Estrutura vazia!")
        return

    if estrutura == "PILHA":
        valor = dados.pop()

    elif estrutura == "FILA":
        valor = dados.pop(0)

    else:
        valor = dados[inicio]
        dados[inicio] = None
        inicio = (inicio + 1) % tamanho
        quantidade -= 1

        if quantidade == 0:
            inicio = 0
            global fim
            fim = 0

        print("Valor extraido:", valor)
        return

    quantidade -= 1
    print("Valor extraido:", valor)


# ==========================================
# OBTER CONTEUDO DA ESTRUTURA
# ==========================================

def obter_conteudo():
    if estrutura == "FILA CIRCULAR":
        return [
            dados[(inicio + i) % tamanho]
            for i in range(quantidade)
        ]

    return dados.copy()


# ==========================================
# IMPRIMIR CONTEUDO
# ==========================================

def imprimir_conteudo():
    if estrutura is None:
        print("Crie uma estrutura primeiro!")
    else:
        print("Conteudo:", obter_conteudo())


# ==========================================
# MENU DAS ESTRUTURAS
# ==========================================

def menu_estrutura(tipo):
    while True:
        print("\n========== MENU", tipo, "==========")
        print("1 - Criar estrutura")
        print("2 - Armazenar valor")
        print("3 - Extrair valor")
        print("4 - Imprimir conteudo")
        print("5 - Voltar ao menu principal")

        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            criar_estrutura(tipo)

        elif opcao == "2":
            if estrutura != tipo:
                print("Crie esta estrutura primeiro!")
            else:
                armazenar_valor()

        elif opcao == "3":
            if estrutura != tipo:
                print("Crie esta estrutura primeiro!")
            else:
                extrair_valor()

        elif opcao == "4":
            if estrutura != tipo:
                print("Crie esta estrutura primeiro!")
            else:
                imprimir_conteudo()

        elif opcao == "5":
            break

        else:
            print("Opcao invalida!")


# ==========================================
# BUBBLE SORT
# ==========================================

def bubble_sort(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


# ==========================================
# SELECTION SORT
# ==========================================

def selection_sort(lista):
    n = len(lista)

    for i in range(n):
        menor = i

        for j in range(i + 1, n):
            if lista[j] < lista[menor]:
                menor = j

        lista[i], lista[menor] = lista[menor], lista[i]


# ==========================================
# INSERTION SORT
# ==========================================

def insertion_sort(lista):
    for i in range(1, len(lista)):
        valor = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > valor:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = valor


# ==========================================
# MENU DE ORDENACAO
# ==========================================

def ordenar(tipo):
    global dados, inicio, fim

    lista = obter_conteudo()

    print("\nConteudo antes da ordenacao:", lista)

    if tipo == "1":
        bubble_sort(lista)
        print("Algoritmo utilizado: Bubble Sort")

    elif tipo == "2":
        selection_sort(lista)
        print("Algoritmo utilizado: Selection Sort")

    elif tipo == "3":
        insertion_sort(lista)
        print("Algoritmo utilizado: Insertion Sort")

    if estrutura == "FILA CIRCULAR":
        dados = [None] * tamanho

        for i in range(len(lista)):
            dados[i] = lista[i]

        inicio = 0
        fim = quantidade % tamanho

    else:
        dados[:] = lista

    print("Conteudo depois da ordenacao:", obter_conteudo())


def menu_ordenacao():
    if estrutura is None:
        print("\nNenhuma estrutura foi criada!")
        print("Escolha primeiro PILHA, FILA ou FILA CIRCULAR.")
        return

    while True:
        print("\n========== MENU ORDENAR ==========")
        print("1 - Bubble Sort")
        print("2 - Selection Sort")
        print("3 - Insertion Sort")
        print("4 - Voltar ao menu principal")

        opcao = input("Escolha um algoritmo: ")

        if opcao in ["1", "2", "3"]:
            ordenar(opcao)

        elif opcao == "4":
            break

        else:
            print("Opcao invalida!")


# ==========================================
# MENU PRINCIPAL
# ==========================================

while True:
    print("\n========== MENU PRINCIPAL ==========")
    print("1 - PILHA")
    print("2 - FILA")
    print("3 - FILA CIRCULAR")
    print("4 - ORDENAR")
    print("5 - SAIR")
    print("====================================")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        menu_estrutura("PILHA")

    elif opcao == "2":
        menu_estrutura("FILA")

    elif opcao == "3":
        menu_estrutura("FILA CIRCULAR")

    elif opcao == "4":
        menu_ordenacao()

    elif opcao == "5":
        print("Programa encerrado. Obrigado!")
        break

    else:
        print("Opcao invalida! Tente novamente.")
