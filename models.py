import main

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

def relatorio():
    return

def grafico():
    return

def estatistica():
    return

def validar_entrada():
    return