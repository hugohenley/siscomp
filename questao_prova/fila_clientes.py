#!/usr/bin/python
# -*- coding: utf-8 -*-

#Classes possíveis: top, master e pop
#Clientes master só são atendidos quando não existem clientes top esperando
#Clientes pop só são atendidos quando não existem clientes master esperando
#Prioridade: Top > Master > Pop

import random

TOTAL_CLIENTES = range(1, 20)
TEMPO_DE_ATENDIMENTO = range(1, 10)
CLASSES_POSSIVEIS = ['top', 'master', 'pop']

clientes_por_classe = {'top': [], 'master':[], 'pop': []}
tempo_por_cliente = {'top': [], 'master':[], 'pop': []}
fila_top = []
fila_master = []
fila_pop = []

def sortear_classe(numero_clientes):
    for n in numero_clientes:
        clientes_por_classe[random.choice(CLASSES_POSSIVEIS)].append(n)

def gerar_fila():
    clientes = range(1, 20)
    random.shuffle(clientes)
    return clientes

def eh_cliente_top(cliente):
    if cliente in clientes_por_classe['top']:
        return True
    else:
        return False

def eh_cliente_master(cliente):
    if cliente in clientes_por_classe['master']:
        return True
    else:
        return False


def organizar_fila(fila):
    for f in fila:
        if eh_cliente_master(f):
            fila_master.append(f)
        elif eh_cliente_top(f):
            fila_top.append(f)
        else:
            fila_pop.append(f)

def atender_clientes(fila_top, fila_master, fila_pop):
    for top in fila_top:
        tempo_atendimento = random.choice(TEMPO_DE_ATENDIMENTO)
        tempo_por_cliente['top'].append(tempo_atendimento + maior_tempo(tempo_por_cliente['top']))

    for master in fila_master:
        tempo_atendimento = random.choice(TEMPO_DE_ATENDIMENTO)
        if master == fila_master[0]:
            tempo_por_cliente['master'].append(tempo_atendimento + maior_tempo(tempo_por_cliente['top']))
        else:
            tempo_por_cliente['master'].append(tempo_atendimento + maior_tempo(tempo_por_cliente['master']))

    for pop in fila_pop:
        tempo_atendimento = random.choice(TEMPO_DE_ATENDIMENTO)
        if pop == fila_pop[0]:
            tempo_por_cliente['pop'].append(tempo_atendimento + maior_tempo(tempo_por_cliente['master']))
        else:
            tempo_por_cliente['pop'].append(tempo_atendimento + maior_tempo(tempo_por_cliente['pop']))

def maior_tempo(lista):
    try:
        return max(lista)
    except:
        return 0

def calcular_turnaround(fila):
    numerador = 0
    denominador = len(fila)
    for f in fila:
        numerador += f
    return str(numerador / denominador)

sortear_classe(TOTAL_CLIENTES)
fila = gerar_fila()
organizar_fila(fila)
atender_clientes(fila_top, fila_master, fila_pop)

print tempo_por_cliente

print 'O tempo médio de turnaround para clientes top é de: ' + calcular_turnaround(tempo_por_cliente['top']) + ' minutos'
print 'O tempo médio de turnaround para clientes master é de: ' + calcular_turnaround(tempo_por_cliente['master']) + ' minutos'
print 'O tempo médio de turnaround para clientes pop é de: ' + calcular_turnaround(tempo_por_cliente['pop']) + ' minutos'