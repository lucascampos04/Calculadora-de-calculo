import numpy as np
import math 
import tkinter as tk
from tkinter import messagebox

def calculandoLambda():
    print("TEORIA DAS FILAS \n")
    print("Vamos começar encontrando o valor de lambda. \nPara encontrar o valor de lambda, eu irei precisar do número de chegadas e do tempo total.")

    tempoTotal = float(input("Tempo total: "))
    numeroDechegadas = float(input("Número de chegadas no servidor/fila: "))
    resultadoLambda = numeroDechegadas / tempoTotal
    print("O valor de lambda é: ", resultadoLambda)

    print("Agora vamos encontrar o valor de MI. \nPara encontrar o valor de MI, é preciso do número de atendimentos e do tempo total.")
    numeroDePessoasAtendidas = float(input("Pessoas atendidas: "))
    tempoTotalMi = float(input("Tempo total: "))
    resultadoMi = numeroDePessoasAtendidas / tempoTotalMi
    print("O valor de MI é: ", resultadoMi, "\n")

    print(f"Lambda: {resultadoLambda} \nMi: {resultadoMi}")

    l = resultadoLambda / (resultadoMi - resultadoLambda)
    lq = (resultadoLambda ** 2) / (resultadoMi * (resultadoMi - resultadoLambda))
    ln = resultadoLambda * (resultadoMi - resultadoLambda)
    p = resultadoLambda / resultadoMi
    w = 1 / (resultadoMi - resultadoLambda)
    wq = resultadoLambda / (resultadoMi * (resultadoMi - resultadoLambda))
    wn =  1 / (resultadoMi - resultadoLambda)

    tempoMedioDechegadasNafila = 1 / resultadoLambda
    tempoMedioDeAtendimento = 1 / resultadoMi
    numeroProvavelNoSistema = l
    numeroProvavelnaFila = lq
    numeroProvavelnaFilaNaoVazia = ln
    ocupacaoNosistema = p
    probabilidadeDoSistemaestarVazio = 1 - p
    probabilidadeDaFilaestarVazia = 1 - (p**2)
    tempoProavvelnoSistema = w
    tempoProvavelnaFila = wq
    tempoProvavelNaFilaNaovazia = wn

    Wq = lq / (numeroDechegadas - resultadoLambda)
    W = Wq + (1 / resultadoMi)
    L = l + resultadoLambda
    Lq = lq + (resultadoLambda**2) / (resultadoMi * (numeroDechegadas - resultadoLambda))

    print("Resultados: \n \n")

    print("Tempo Médio de chegadas na fila: ", tempoMedioDechegadasNafila)
    print("Tempo Médio de Atendimento: ", tempoMedioDeAtendimento)
    print("Número provável no sistema: ", numeroProvavelNoSistema)
    print("Número provável na fila: ", numeroProvavelnaFila)
    print("Número provável na fila não vazia: ", numeroProvavelnaFilaNaoVazia)
    print("Ocupação no sistema: ", ocupacaoNosistema)
    print("Probabilidade do sistema estar vazio: ", probabilidadeDoSistemaestarVazio)
    print("Probabilidade da fila estar vazia: ", probabilidadeDaFilaestarVazia)
    print("Tempo provável no sistema: ", tempoProavvelnoSistema)
    print("Tempo provável na fila: ", tempoProvavelnaFila)
    print("Tempo provável na fila não vazia: ", tempoProvavelNaFilaNaovazia)
    print("Tempo médio de espera na fila (Wq): ", Wq)
    print("Tempo médio de resposta no sistema (W): ", W)
    print("Número médio de clientes no sistema (L): ", L)
    print("Número médio de clientes na fila (Lq): ", Lq)

    # Disciplina de fila: FIFO
    tempoMedioEsperaFIFO = tempoProvavelnaFila
    print("Tempo médio de espera na fila (FIFO): ", tempoMedioEsperaFIFO)

    # Disciplina de fila: LIFO (ou FILO)
    tempoMedioEsperaLIFO = tempoMedioDechegadasNafila
    print("Tempo médio de espera na fila (LIFO): ", tempoMedioEsperaLIFO)

    # Disciplina de fila: LEFO
    tempoMedioEsperaLEFO = tempoMedioDeAtendimento
    print("Tempo médio de espera na fila (LEFO): ", tempoMedioEsperaLEFO)

def binario_para_decimal(binario):
    decimal = 0
    for digito in binario:
        decimal = decimal * 2 + int(digito)
    return decimal

def converter_binario_decimal():
    binario = input("Digite um número binário: ")
    decimal = binario_para_decimal(binario)
    print(f"Binário: {binario} -> Decimal: {decimal}")

def decimal_para_binario(decimal):
    binario = ""
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return binario

def converter_decimal_binario():
    decimal = int(input("Digite um número decimal: "))
    binario = decimal_para_binario(decimal)
    print(f"Decimal: {decimal} -> Binário: {binario}")

def juros_composto():
    valor_inicial = float(input("Valor inicial: "))
    taxa_juros = float(input("Taxa de juros: "))
    periodo = float(input("Período: "))

    taxa_decimal = taxa_juros / 100
    
    valor_final = valor_inicial * (1 + taxa_decimal) ** periodo
    
    print("O valor final com juros compostos é R$:", round(valor_final, 2))

def juros_simples():
    valor_inicial = float(input("Valor inicial: "))
    taxa_juros = float(input("Taxa de juros: "))
    periodo = float(input("Período: "))

    taxa_decimal = taxa_juros / 100

    valor_final = valor_inicial * (1 + (taxa_decimal * periodo))

    print("O valor final com juros simples é R$:", round(valor_final, 2))

def calcular_media_e_desvio_padrao():
    def calcular_media():
        dados = input("Insira os dados separados por espaço: ").split()
        dados = [float(x) for x in dados]
        soma = sum(dados)
        media = soma / len(dados)
        return media

    def calcular_desvio_padrao():
        media = calcular_media()  
        dados = input("Insira os dados separados por espaço: ").split()
        dados = [float(x) for x in dados]
        soma_diferencas_quadrados = sum((x - media) ** 2 for x in dados)
        desvio_padrao = (soma_diferencas_quadrados / len(dados)) ** 0.5
        return desvio_padrao
    
    def calcular_probabilidade():
        evento_favoravel = float(input("Insira o numero de eventos favoraveis: "))
        evento_amostral = float(input("Insira o numero do espaço amostral"))
        probabilidade = evento_favoravel / evento_amostral
        return probabilidade

    media = calcular_media()
    print("A média é: ", media)
    desvio_padrao = calcular_desvio_padrao()
    print("O desvio padrão é: ", desvio_padrao)
    probabilidade = calcular_probabilidade()
    print("Probabilidade: ", probabilidade)

def trigonometria():
    def calular_trigonometria():
        angulo = float(input("Insira o valor do angulo em graus: "))
        radianos = math.radians(angulo)
        cos = math.cos(radianos)
        sen = math.sin(radianos)
        tan = math.tan(radianos)
        return cos, sen, tan
    
    resultado = calular_trigonometria()
    print("Cosseno: ", resultado[0])
    print("Seno: ", resultado[1])
    print("Tangente: ", resultado[2])
    
def bhaskara():
    a = float(input("Insira o valor de a: "))
    b = float(input("Insira o valor de b: "))
    c = float(input("Insira o valor de c: "))
    delta = b**2 - 4 * a * c
    x1 = -b + np.sqrt(delta) / 2 * a
    x2 = -b - np.sqrt(delta) / 2 * a
    
    print(f"x1: {x1}\nx2: {x2}")

def vetoresContasBasicas():
    def soma_vetores():
        print("Soma de vetores")
        a1 = float(input("Valor de a1: "))
        a2 = float(input("Valor de a2: "))
        a3 = float(input("Valor de a3: "))
        b1 = float(input("Valor de b1: "))
        b2 = float(input("Valor de b2: "))
        b3 = float(input("Valor de b3: "))
        somando_ab = (a1 + b1, a2 + b2, a3 + b3)
        return somando_ab
    resultado_soma = soma_vetores()
    print("Resultado da soma dos vetores: ", resultado_soma)
    
    def subtraindo_vetores():
        print("\nSubtração de vetores")
        a1 = float(input("Valor de a1: "))
        a2 = float(input("Valor de a2: "))
        a3 = float(input("Valor de a3: "))
        b1 = float(input("Valor de b1: "))
        b2 = float(input("Valor de b2: "))
        b3 = float(input("Valor de b3: "))
        subtraindo_ab = (a1 - b1, a2 - b2, a3 - b3)
        return subtraindo_ab
    resultado_sub = subtraindo_vetores()
    print("Resultado da subtração dos vetores: ", resultado_sub)

    def multiplicando_por_escalar_vetores():
        print("\nMultiplicação de vetores")
        escalar = float(input("Valor do escalar: "))
        a1 = float(input("Valor de a1: "))
        a2 = float(input("Valor de a2: "))
        a3 = float(input("Valor de a3: "))
        multiplicando_vetor = (escalar*a1, escalar*a2, escalar*a3)
        return multiplicando_vetor
    multipli_vetor = multiplicando_por_escalar_vetores()
    print("Resultado da multiplicação escalar dos vetores: ", multipli_vetor)

    def produto_escalar_interno():
        print("\nVetor de produto escalar interno")
        a1 = float(input("Valor de a1: "))
        a2 = float(input("Valor de a2: "))
        a3 = float(input("Valor de a3: "))
        b1 = float(input("Valor de b1: "))
        b2 = float(input("Valor de b2: "))
        b3 = float(input("Valor de b3: "))
        produto_escalar_inter = ((a1*b1) + (a2*b2) + (a3*b3))
        return produto_escalar_inter
    produto_escalar_inter = produto_escalar_interno()
    print("Resultado da multiplicação de um produto escalar interno: ", produto_escalar_inter)
    
    def produto_escalar_externo():
        print("\nVetor de produto vetorial")
        a1 = float(input("Valor de a1: "))
        a2 = float(input("Valor de a2: "))
        a3 = float(input("Valor de a3: "))
        b1 = float(input("Valor de b1: "))
        b2 = float(input("Valor de b2: "))
        b3 = float(input("Valor de b3: "))
        c1 = a2 * b3 - a3 * b2
        c2 = a3 * b1 - a1 * b3
        c3 = a1 * b2 - a2 * b1
        vetor_vetorial = [c1, c2, c3]
        resultado = [float(x) for x in vetor_vetorial]
        return resultado
    resultado = produto_escalar_externo()
    print("Resultado do vetor escalar externo: ", resultado)
    print("")
    
    resultados_vetores = [resultado_soma, resultado_sub, multipli_vetor, produto_escalar_inter, resultado]
    print(f"Soma: {resultados_vetores[0]} \nSubtração: {resultados_vetores[1]} \nMultiplicação: {resultados_vetores[2]} \nVetor interno: {resultados_vetores[3]} \nVetor externo: {resultados_vetores[4]}")

def vetores():
    def moduloDeVetores():
        print("Coloque os valores de v1 e v2 separadamente: ")
        valoresV1 = input("V1: ").split()
        v1 = [float(x) for x in valoresV1]
        valoresV2 = input("V2: ").split()
        v2 = [float(y) for y in valoresV2]
        moduloV1 = np.sqrt(sum([x**2 for x in v1]))
        moduloV2 = np.sqrt(sum([y**2 for y in v2]))
        return v1, v2, moduloV1, moduloV2
    
    def anguloTeta():
        print("Coloque os vetores separadamente: ")
        vetoresV1 = input("V1: ").split()
        v1 = [float(x) for x in vetoresV1]
        vetoresV2 = input("V2: ").split()
        v2 = [float(y) for y in vetoresV2]
        moduloV1 = np.sqrt(sum(x**2 for x in v1))
        moduloV2 = np.sqrt(sum(y**2 for y in v2))
        produto_escalar = np.dot(v1, v2)
        cos_teta = produto_escalar / (moduloV1 * moduloV2)
        angulo = np.arccos(cos_teta) * 180 / np.pi
        return angulo 
    resultado = moduloDeVetores()
    angulo = anguloTeta()
    print(f"Vetores: {resultado[0]}, {resultado[1]}\nResultado V1: {resultado[2]}\nResultado V2: {resultado[3]}")
    print(f"Ângulo entre os vetores: {angulo} graus")

    def projecaoOrtogonal():
        print("Coloque os valores de w separadamente: ")
        valoresW = input("W: ").split()
        w = [float(x) for x in valoresW]
        print("Coloque os valores de u separadamente: ")
        valoresU = input("U: ").split()
        u = [float(y) for y in valoresU]
        produto_escalar = np.dot(w, u)
        u_norm_squared = np.dot(u, u)
        resultado = (produto_escalar / u_norm_squared) * np.array(u)
        return resultado

    resultado_proje = projecaoOrtogonal()
    print("Resultado da projeção ortogonal: ", resultado_proje)

def matriz():
    escolher = int(input("Soma :\n1 - 2x2 | 2 - 3x3:\nSubtração:\n3 - 2x2 | 4 - 3x3:\nMultiplicação:\n5 - 2x2 | 6 - 3x3:\n7 i Transposta:  "))

    if escolher == 1:
        def somaMatriz2x2():
            a11_matriz1 = float(input("Valor de a11: "))
            a12_matriz1 = float(input("Valor de a12: "))
            a21_matriz1 = float(input("Valor de a21: "))
            a22_matriz1 = float(input("Valor de a22: "))

            return [a11_matriz1, a12_matriz1, a21_matriz1, a22_matriz1]

        matriz1 = somaMatriz2x2()
        matriz2 = somaMatriz2x2()

        soma = [a + b for a, b in zip(matriz1, matriz2)]

        resultado_final = matriz1, matriz2, soma
        print(f"Matriz 1: {resultado_final[0]}")
        print(f"Matriz 2: {resultado_final[1]}")
        print(f"Soma: {resultado_final[2]}")

    elif escolher == 2:
        def matriz3x3():
            a11_matriz1 = float(input("Valor de a11: "))
            a12_matriz1 = float(input("Valor de a12: "))
            a13_matriz1 = float(input("Valor de a13: "))
            a21_matriz1 = float(input("Valor de a21: "))
            a22_matriz1 = float(input("Valor de a22: "))
            a23_matriz1 = float(input("Valor de a23: "))
            a31_matriz1 = float(input("Valor de a31: "))
            a32_matriz1 = float(input("Valor de a32: "))
            a33_matriz1 = float(input("Valor de a33: "))

            return [a11_matriz1, a12_matriz1, a13_matriz1, a21_matriz1, a22_matriz1, a23_matriz1, a31_matriz1, a32_matriz1, a33_matriz1]

        matriz1 = matriz3x3()
        matriz2 = matriz3x3()

        soma = [a + b for a, b in zip(matriz1, matriz2)]

        resultado_final = matriz1, matriz2, soma
        print(f"Matriz 1: {resultado_final[0]}")
        print(f"Matriz 2: {resultado_final[1]}")
        print(f"Soma: {resultado_final[2]}")
    elif escolher == 3:
        def subtracaoMatriz2x2():
            a11_matriz1 = float(input("Valor de a11: "))
            a12_matriz1 = float(input("Valor de a12: "))
            a21_matriz1 = float(input("Valor de a21: "))
            a22_matriz1 = float(input("Valor de a22: "))

            a11_matriz2 = float(input("Valor de a11: "))
            a12_matriz2 = float(input("Valor de a12: "))
            a21_matriz2 = float(input("Valor de a21: "))
            a22_matriz2 = float(input("Valor de a22: "))

            resultado = [
                a11_matriz1 - a11_matriz2,
                a12_matriz1 - a12_matriz2,
                a21_matriz1 - a21_matriz2,
                a22_matriz1 - a22_matriz2
            ]
            return resultado
        resultado_subtracao = subtracaoMatriz2x2()
        print("Resultado da subtração:")
        print(resultado_subtracao)
    elif escolher == 4:
        def subtracaoMatriz3x3():
            a11_matriz1 = float(input("Valor de a11: "))
            a12_matriz1 = float(input("Valor de a12: "))
            a11_matriz1 = float(input("Valor de a11: "))
            a12_matriz1 = float(input("Valor de a12: "))
            a13_matriz1 = float(input("Valor de a13: "))
            a21_matriz1 = float(input("Valor de a21: "))
            a22_matriz1 = float(input("Valor de a22: "))
            a23_matriz1 = float(input("Valor de a23: "))
            a31_matriz1 = float(input("Valor de a31: "))
            a32_matriz1 = float(input("Valor de a32: "))
            a33_matriz1 = float(input("Valor de a33: "))

            a11_matriz2 = float(input("Valor de a11: "))
            a12_matriz2 = float(input("Valor de a12: "))
            a13_matriz2 = float(input("Valor de a13: "))
            a21_matriz2 = float(input("Valor de a21: "))
            a22_matriz2 = float(input("Valor de a22: "))
            a23_matriz2 = float(input("Valor de a23: "))
            a31_matriz2 = float(input("Valor de a31: "))
            a32_matriz2 = float(input("Valor de a32: "))
            a33_matriz2 = float(input("Valor de a33: "))

            resultado = [
                a11_matriz1 - a11_matriz2,
                a12_matriz1 - a12_matriz2,
                a13_matriz1 - a13_matriz2,
                a21_matriz1 - a21_matriz2,
                a22_matriz1 - a22_matriz2,
                a23_matriz1 - a23_matriz2,
                a31_matriz1 - a31_matriz2,
                a32_matriz1 - a32_matriz2,
                a33_matriz1 - a33_matriz2
            ]

            return resultado

        resultado_subtracao = subtracaoMatriz3x3()
        print("Resultado da subtração:")
        print(resultado_subtracao)

    elif escolher == 5:
        def multiplicacao2x2():
            a11_matriz1 = float(input("Valor de a11: "))
            a12_matriz1 = float(input("Valor de a12: "))
            a21_matriz1 = float(input("Valor de a21: "))
            a22_matriz1 = float(input("Valor de a22: "))

            a11_matriz2 = float(input("Valor de a11: "))
            a12_matriz2 = float(input("Valor de a12: "))
            a21_matriz2 = float(input("Valor de a21: "))
            a22_matriz2 = float(input("Valor de a22: "))

            resultado = [
                a11_matriz1 * a11_matriz2 + a12_matriz1 * a21_matriz2,
                a11_matriz1 * a12_matriz2 + a12_matriz1 * a22_matriz2,
                a21_matriz1 * a11_matriz2 + a22_matriz1 * a21_matriz2,
                a21_matriz1 * a12_matriz2 + a22_matriz1 * a22_matriz2
            ]
            return resultado
        resultado_final = multiplicacao2x2()
        print(f"O resultado da multiplicação {resultado_final}")
    elif escolher == 6:
        def multiplicacao3x3():
            a11_matriz1 = float(input("Valor de a11: "))
            a12_matriz1 = float(input("Valor de a12: "))
            a13_matriz1 = float(input("Valor de a13: "))
            a21_matriz1 = float(input("Valor de a21: "))
            a22_matriz1 = float(input("Valor de a22: "))
            a23_matriz1 = float(input("Valor de a23: "))

            a11_matriz2 = float(input("Valor de a11: "))
            a12_matriz2 = float(input("Valor de a12: "))
            a13_matriz2 = float(input("Valor de a13: "))
            a21_matriz2 = float(input("Valor de a21: "))
            a22_matriz2 = float(input("Valor de a22: "))
            a23_matriz2 = float(input("Valor de a23: "))

            resultado = [
                a11_matriz1 * a11_matriz2 + a12_matriz1 * a21_matriz2,
                a11_matriz1 * a12_matriz2 + a12_matriz1 * a22_matriz2,
                
                a21_matriz1 * a11_matriz2 + a22_matriz1 * a21_matriz2,
                a21_matriz1 * a12_matriz2 + a22_matriz1 * a22_matriz2
            ]

            return resultado
        resultado_subtracao = subtracaoMatriz3x3()
        print("Resultado da subtração:")
        print(resultado_subtracao)
    elif escolher == 7:
        def matriz_transposta(matriz):
            transposta = [
                matriz[0], matriz[3], matriz[6], 
                matriz[1], matriz[4], matriz[7],            
                matriz[2], matriz[5], matriz[8]
            ]
            return transposta

        def matriz3x3():
            a11 = float(input("Valor de a11: "))
            a12 = float(input("Valor de a12: "))
            a13 = float(input("Valor de a13: "))
            a21 = float(input("Valor de a21: "))
            a22 = float(input("Valor de a22: "))
            a23 = float(input("Valor de a23: "))
            a31 = float(input("Valor de a31: "))
            a32 = float(input("Valor de a32: "))
            a33 = float(input("Valor de a33: "))

            return [a11, a12, a13, a21, a22, a23, a31, a32, a33]

        matriz = matriz3x3()
        transposta = matriz_transposta(matriz)

        print("Matriz original:")
        print(matriz)
        print("Matriz transposta:")
        print(transposta)


# INTERFACES 
def tela_teoria_das_filas():
    teoria_filas = tk.Tk() 
    teoria_filas.title("Teoria da filas")

def tela_juros_composto():
    juros_composto = tk.Tk()
    juros_composto.title("Juros composto")

def tela_juros_simples():
    juros_composto = tk.Tk()
    juros_composto.title("Juros composto")

def tela_vetores():
    vetores = tk.Tk()
    vetores.title("Vetores")

def tela_matrizes():
    matrizes = tk.Tk()
    matrizes.title("Matrizes")

def tela_trigonometria():
    trigonometria = tk.Tk()
    trigonometria.title("Trigonometria")
# ---------------------------- #
# ---------- cores ----------- #

cor1 = "#FF0000"  # Vermelho
cor2 = "#00FF00"  # Verde
cor3 = "#0000FF"  # Azul
cor4 = "#FFFF00"  # Amarelo
cor5 = "#FF00FF"  # Magenta
cor6 = "#00FFFF"  # Ciano
cor7 = "#FFA500"  # Laranja
cor8 = "#800080"  # Roxo
cor9 = "#008000"  # Verde Escuro
cor10 = "#000080"  # Azul Escuro

window = tk.Tk()
window.title("Calculadora")
window.geometry("300x400")
window.configure(bg=cor10)

btn_teoria_das_filas = tk.Button(window,height=1, width=15,text="teoria das filas", highlightbackground=cor7, font=("Arial", 12, "bold"), command=tela_teoria_das_filas)
btn_teoria_das_filas.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

btn_juros_composto = tk.Button(window,height=1, width=15,text="Juros composto", highlightbackground=cor7, font=("Arial", 12, "bold"), command=tela_juros_composto)
btn_juros_composto.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

btn_juros_simples = tk.Button(window,height=1, width=15,text="Juros simples", highlightbackground=cor7, font=("Arial", 12, "bold"), command=tela_juros_simples)
btn_juros_simples.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

btn_vetores = tk.Button(window,height=1, width=15,text="Vetores", highlightbackground=cor7, font=("Arial", 12, "bold"), command=tela_vetores)
btn_vetores.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

btn_matrizes = tk.Button(window,height=1, width=15,text="Matriz", highlightbackground=cor7, font=("Arial", 12, "bold"), command=tela_matrizes)
btn_matrizes.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

btn_trigonometria = tk.Button(window,height=1, width=15,text="Trigonometria", highlightbackground=cor7, font=("Arial", 12, "bold"), command=tela_trigonometria)
btn_trigonometria.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

window.mainloop()

        












