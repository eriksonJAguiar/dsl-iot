#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import psutil
import time
import pandas as pd
import os


CPUUsage = []
tempoDecorrido = []
usoMemoria = []
restAPI = []
tempo = 0

def headLista(lista):
    return lista[0]


for i in range(200):
    #Coluna da memória utilizada (em GB)
    a = dict(psutil.virtual_memory()._asdict())
    value = (a['used']/a['total'])*100
    print(value)
    usoMemoria.append(value)
    
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
tabela.insert(1, "Memoria Utilizada (%)", usoMemoria)
tabela.insert(2, "CPU Utilizada (%)", CPUUsage)



    
tabela.to_csv("./desempenho_hw_sem_ruido.csv")
