

def listar(treinos, tipo):
    i = 1
    for treino in treinos:
        if treino["tipo"].lower() == tipo.lower():
            print(f"Treino {i}: {treino}")
            i += 1

def semana_ideal(treinos):
    return

def dia_ideal(treinos):
    if not treinos:
        return None

    dias = {}
    for treino in treinos:
        data = treino["data"]
        if data not in dias:
            dias[data]= {"duracao_total": 0, "calorias_totais": 0, "quantidade_treinos": 0}
        dias[data]["duracao_total"] += treino["duracao"]
        dias[data]["calorias_totais"] += treino["calorias"]
        dias[data]["quantidade_treinos"] += 1

    melhor_dia = ''
    maior_caloria = -1
    for data, info in dias.items():
        if info["calorias_totais"]> maior_caloria:
            maior_caloria = info["calorias_totais"]
            melhor_dia = data
    return {
        "data": melhor_dia,
        "quantidade_treinos": dias[melhor_dia]["quantidade_treinos"],
        "duracao_total": dias[melhor_dia]["duracao_total"],
        "calorias_totais": dias[melhor_dia]["calorias_totais"]
    }

def media_semanal(treinos):
    return

def treino_mais_longo(treinos):
    if not treinos:
        return None
    maior_duracao = 0
    maior_treino = {}
    for treino in treinos:
        if treino["duracao"] > maior_duracao:
            maior_treino = treino
            maior_duracao = maior_treino["duracao"]
    return maior_treino

def calcular_total_calorias(treinos): 
    total = 0
    for treino in treinos:
        total += treino["calorias"]
    return total

def calcular_total_minutos(treinos):
    total = 0
    for treino in treinos:
        total += treino["duracao"]
    return total

def media_esforco(treinos):
    if not treinos:
        return 0.0

    esforcos = [treino["esforco"] for treino in treinos]
    media = sum(esforcos) / len(esforcos)
    
    return round(media, 2)