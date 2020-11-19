#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import psutil
import time
import pandas as pd
import os

#Diretório certo
#os.chdir('/home/grupo_jo/Downloads/codigo_tcc_fernando_final-20201119T152734Z-001/codigo_tcc_fernando_final')

CPUUsage = []
tempoDecorrido = []
usoMemoria = []
restAPI = []

def headLista(lista):
    return lista[0]

for i in range(600):
    #Coluna da memória utilizada (em GB)
    a = dict(psutil.virtual_memory()._asdict())
    print(a['used'])
    usoMemoria.append(a['used']/1073741824)
    
    #Coluna do percentual de CPU usado
    b = psutil.cpu_percent()
    print(b)
    CPUUsage.append(b)
    
    #Coluna do tempo decorrido
    tempoDecorrido.append(tempo)
    print(tempo)
    
    #Espera um segundo
    time.sleep(1)
    
    #Incrementa o tempo
    tempo = tempo + 1
    
tabela = pd.DataFrame()

tabela.insert(0, "Tempo", tempoDecorrido)
tabela.insert(1, "Memoria Utilizada (GB)", usoMemoria)
tabela.insert(2, "Percentual Global de Processamento Utilizado", CPUUsage)



    
tabela.to_csv("./desempenho_hw.csv")