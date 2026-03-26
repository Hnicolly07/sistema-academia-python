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
        
        if escolha in [2,3,4,5,6,7,8] and not treinos:
            print('Não há treinos registrados. Favor registrar ao menos um treino (Opção 1)')
            continue

        match escolha:
            case 1:
                data = input('Data: ')
                while True:
                    semana = int(input('Esse treino pertence a qual semana do mês (1-4)? '))
                    if semana in [1,2,3,4]:
                        break
                    print('Apenas valores entre 1 e 4. Tente Novamente!')
                tipo_treino = input('Tipo de treino: ')
                duracao = int(input('Duração: '))
                esforco_percebido = int(input('Esforço percebido: '))
                while esforco_percebido not in [1,2,3,4,5,6,7,8,9,10]:
                    print("Apenas valores de 1 a 10. Digite novamente!")
                    esforco_percebido = int(input('Esforço percebido: '))
                calorias_estimadas = int(input('Calorias estimadas: '))
                novo_treino = models.registrar_sessao(data, semana, tipo_treino, duracao, esforco_percebido, calorias_estimadas)
                treinos.append(novo_treino)
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
                services.semana_ideal(treinos)
            case 4:
                services.dia_ideal(treinos)
            case 5:
                services.media_semanal(treinos)
            case 6:
                print(f"Treino mais longo: {services.treino_mais_longo(treinos)}")
            case 7:
                models.resumo(treinos)
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