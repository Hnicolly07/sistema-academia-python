import main

def listar(treinos, tipo):
    i = 1
    for treino in treinos:
        if treino["tipo"].lower() == tipo.lower():
            print(f"Treino {i}: {treino}")
            i += 1

def semana_ideal():
    return

def dia_ideal():
    return

def media_semanal():
    return

def treino_mais_longo():
    return

def calcular_total_calorias(treinos): 
    total = 0
    for treino in treinos:
        total += treino["calorias"]
    return total

def calcular_total_minutos():
    return

def media_esforco():
    return