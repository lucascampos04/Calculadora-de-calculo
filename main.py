import numpy as np
import math 

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
    escolher = input("1 - 2x2 | 2 - 3x3")
    if escolher == 1:
        print("Hello word")
    elif escolher == "2":
        print("Hello word")
        












