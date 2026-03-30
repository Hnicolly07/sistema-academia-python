import models, services 

def main():
    novo_treino = {}
    treinos = []
    while True:
        exibir_menu()
        try:
            escolha = int(input())
        except ValueError:
            print('Digite apenas números')
            continue

        if not models.validar_escolha(escolha):
            print('Opção Inválida. Tente Novamente!')
            continue

        if escolha == 0:
            print('Encerrando...')
            break
        
        if escolha in [2,3,4,5,6,7,8,9] and not treinos:
            print('Não há treinos registrados. Favor registrar ao menos um treino (Opção 1)')
            continue

        match escolha:
            case 1:
                data = models.validar_str('Dia da Semana: ')
                while not models.validar_dia_semana(data):
                    print("Dia Inválido")
                    data = models.validar_str('Dia da Semana: ')
                semana = models.validar_intervalo('Esse treino pertence a qual semana do mês (1-4)? ', 1, 4)
                tipo_treino = models.validar_str('Tipo de treino: ')
                duracao = models.validar_inteiro('Duração: ')
                esforco_percebido = models.validar_intervalo('Esforço percebido (1-10): ', 1, 10)
                calorias_estimadas = models.validar_inteiro('Calorias estimadas: ')
        
                novo_treino = models.registrar_sessao(data, semana, tipo_treino, duracao, esforco_percebido, calorias_estimadas)
                treinos.append(novo_treino)
                print('\nTreino cadastrado com sucesso!')
            case 2:
                tipo_desejado = input('Tipo de treino que deseja listar: ')
                existe = False
                for treino in treinos:
                    if treino["tipo"].lower() == tipo_desejado.lower():
                        existe = True
                        break #break porque só precisa encontrar 1 vez p/ saber que tem
                else:
                    print(f"Não há treinos do tipo {tipo_desejado} no sistema")
                        
                if existe:
                    services.listar(treinos, tipo_desejado)
            case 3:
                print(f"\nSEMANA IDEAL: {services.semana_ideal(treinos)}")
            case 4:
                melhor_dia = services.dia_ideal(treinos)
                print("\n" + "-"*30)
                print("SEU DIA IDEAL (Recorde)")
                print("-"*30)
                print(f"Data: {melhor_dia['data']}")
                print(f"Treinos realizados: {melhor_dia['quantidade_treinos']}")
                print(f"Duração Total: {melhor_dia['duracao_total']} minutos")
                print(f"Calorias Queimadas: {melhor_dia['calorias_totais']} kcal")
                print("-"*30)
            case 5:
                print(f"\nMÉDIA SEMANAL: {services.media_semanal(treinos)}")
            case 6:
                mais_longo = services.treino_mais_longo(treinos)
                print(f"\nTreino mais longo: {mais_longo['tipo']} ({mais_longo['duracao']} min)")
            case 7:
                models.estatistica(treinos)
            case 8:
                models.relatorio(treinos)
            case 9:
                models.grafico(treinos) 
            
                
def exibir_menu():
    print("\n" + "="*45)
    print(" 🏋️  SISTEMA DE ACOMPANHAMENTO DE TREINOS  🏋️")
    print("="*45)
    print("1. Registrar nova sessão")
    print("2. Listar sessões cadastradas")
    print("3. Semana Ideal")
    print("4. Dia Ideal")
    print("5. Média Semanal")
    print("6. Obter treino mais longo")
    print("7. Gerar Resumo")
    print("8. Gerar Relatório")
    print("9. Ver Gráfico de Calorias (Visual)")
    print("0. Sair do sistema")
    print("="*45)

if __name__ == "__main__":
    main()