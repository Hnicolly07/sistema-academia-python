import models, services 

def main():
    novo_treino = {}
    treinos = []
    while True:
        #exibir_menu()
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

        match escolha:
            case 1:
                data = input('Data: ')
                tipo_treino = input('Tipo de treino: ')
                duracao = int(input('Duração: '))
                esforco_percebido = int(input('Esforço percebido: '))
                while esforco_percebido not in [1,2,3,4,5,6,7,8,9,10]:
                    print("Apenas valores de 1 a 10. Digite novamente!")
                    esforco_percebido = int(input('Esforço percebido: '))
                calorias_estimadas = int(input('Calorias estimadas: '))
            case 2:
                services.listar()
            case 3:
                services.semana_ideal()
                
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
    print("8. Gerar Relatório Estatístico")
    print("9. Ver Gráfico de Calorias (Visual)")
    print("0. Sair do sistema")
    print("="*45)

if __name__ == "__main__":
    main()