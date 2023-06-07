import numpy as np

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

# Exemplo de uso
converter_binario_decimal()
converter_decimal_binario()




