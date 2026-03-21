import services
#import numpy as np
def validar_escolha(escolha):
    if escolha in [0,1,2,3,4,5,6,7,8,9]:
        return True
    return False

def registrar_sessao(data, tipo, duracao, esforco, calorias):
    novo_treino = {
        "data": data,
        "tipo": tipo,
        "duracao": duracao,
        "esforco": esforco,
        "calorias": calorias
    }
    
    return novo_treino

def resumo():
    return

def relatorio(treinos):
    if not treinos:
        return None

    total_treinos = len(treinos)
    total_duracao = services.calcular_total_minutos(treinos)
    total_calorias = services.calcular_total_calorias(treinos)
    media = services.media_esforco(treinos)
    mais_longo = services.treino_mais_longo(treinos) #falta fazer função
    dia_campeao = services.dia_ideal(treinos)
    semana_campea = services.semana_ideal(treinos) #falta implementar
    media_semana = services.media_semanal(treinos) #parte de hiorrana, falta fazer - já esta estrutrado só implementar

    return {
        "total_treinos": total_treinos,
        "total_duracao": total_duracao,
        "total_calorias": total_calorias,
        "media_esforco": media,
        "treino_mais_longo": mais_longo,
        "dia_ideal": dia_campeao,
        "semana_ideal": semana_campea,
        "media_semanal": media_semana
    }

def grafico(): #utilização de numpy e/ou matplotlib
    return

def estatistica(treinos): #utilização de numpy e/ou matplotlib
    if len(treinos) == 0:
        print("\nNenhum treino registrado para calcular estatísticas.")
        return None
    
    total_minutos = services.calcular_total_minutos(treinos)
    total_calorias = services.calcular_total_calorias(treinos)
    esforco_medio = services.media_esforco(treinos)
    mais_longo = services.treino_mais_longo(treinos)

    print("\n" + "-"*45)
    print("ESTATÍSTICAS GERAIS")
    print("-"*45)
    print(f"Total de Minutos: {total_minutos}")
    print(f"Total de Calorias: {total_calorias}")
    print(f"Média de Esforço: {esforco_medio}/10")
    print(f"Treino Mais Longo: {mais_longo['tipo']} ({mais_longo['duracao']} min)")
    print("-"*45)

    return {
        "total_minutos": total_minutos,
        "total_calorias": total_calorias,
        "esforco_medio": esforco_medio,
        "treino_mais_longo": mais_longo
    }

def validar_entrada():
    return