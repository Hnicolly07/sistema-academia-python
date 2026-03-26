import services
import pandas as pd
import matplotlib.pyplot as plt

def validar_escolha(escolha):
    if escolha in [0,1,2,3,4,5,6,7,8,9]:
        return True
    return False

def registrar_sessao(data, semana, tipo, duracao, esforco, calorias):
    novo_treino = {
        "data": data,
        "semana": semana,
        "tipo": tipo,
        "duracao": duracao,
        "esforco": esforco,
        "calorias": calorias
    }
    
    return novo_treino

def relatorio(treinos): #talvez passar chamadas pra dentro dos prints pra reduzir utilização de memoria
    total_treinos = len(treinos)
    total_duracao = services.calcular_total_minutos(treinos)
    total_calorias = services.calcular_total_calorias(treinos)
    media = services.media_esforco(treinos)
    mais_longo = services.treino_mais_longo(treinos)
    dia_campeao = services.dia_ideal(treinos)
    semana_campea = services.semana_ideal(treinos) 
    media_semana = services.media_semanal(treinos) 

    print("\n" + "="*50)
    print(" RELATÓRIO GERAL DE TREINOS ")
    print("="*50)
    print(f"Total de Sessões: {total_treinos}")
    print(f"Tempo Total Gasto: {total_duracao} minutos")
    print(f"Total de Calorias Queimadas: {total_calorias} kcal")
    print(f"Média de Esforço Percebido: {media}/10")
                    
    dados = relatorio(treinos)

    if dados['treino_mais_longo']:
        t_longo = dados['treino_mais_longo']
        print(f"Treino Mais Longo: {t_longo['tipo']} ({t_longo['duracao']} min)")
                
    if dados['dia_ideal']:
        print(f"Dia Ideal: {dados['dia_ideal']['data']} ({dados['dia_ideal']['calorias_totais']} kcal)")
                        
    print("-" * 50)
    print(" MÉTRICAS EM DESENVOLVIMENTO ")
                    
                # ainda não está pronto, falta fazer, só pra adiantar e deixar já estruturado.
    if dados['semana_ideal']:
        print(f"Semana Ideal: {services.media_semanal(treinos)}")
    else:
        print(f"Semana Ideal: {services.media_semanal(treinos)}")
                        
    if dados['media_semanal']:
        print(f"Média Semanal: {services.media_semanal(treinos)}")
    else:
        print(f"Média Semanal: {services.media_semanal(treinos)})")

def grafico(treinos): 
    df = pd.DataFrame(treinos)
    calorias_por_tipo = df.groupby('tipo')['calorias'].sum()
    plt.figure(figsize=(10, 6))
    ax = calorias_por_tipo.plot(kind='barh', color='deepskyblue')

    ax.bar_label(ax.containers[0], fontweight='bold', padding=4)

    plt.title('Calorias Queimadas por Tipo de Treino', fontsize=14, fontweight='bold')
    plt.xlabel('Total de Calorias (kcal)', fontsize=12)
    plt.ylabel('Tipo de Treino', fontsize=12)
    plt.xticks(rotation=0)
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()


def estatistica(treinos):
    mais_longo = services.treino_mais_longo(treinos)

    print("\n" + "-"*45)
    print("ESTATÍSTICAS GERAIS")
    print("-"*45)
    print(f"Total de Minutos: {services.calcular_total_minutos(treinos)}")
    print(f"Total de Calorias: {services.calcular_total_calorias(treinos)}")
    print(f"Média de Esforço: {services.media_esforco(treinos)}/10")
    print(f"Treino Mais Longo: {mais_longo['tipo']} ({mais_longo['duracao']} min)")
    print("-"*45)

def validar_entrada():
    return