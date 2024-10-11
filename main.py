import matplotlib.pyplot as plt
from services.analise_solo_service import AnaliseSoloService
from migrations.migration import verificar_e_criar_tabela

def validar_entrada(valor, min_valor, max_valor, nome_campo):
    try:
        valor_float = float(valor)
        if min_valor <= valor_float <= max_valor:
            return valor_float
        else:
            raise ValueError(f"{nome_campo} deve estar entre {min_valor} e {max_valor}")
    except ValueError:
        raise ValueError(f"{nome_campo} deve ser um número válido")

def obter_entrada_usuario(incluir_fertilidade=True):
    pH = validar_entrada(input("pH (0-14): "), 0, 14, "pH")
    umidade = validar_entrada(input("Umidade (%): "), 0, 100, "Umidade")
    temperatura = validar_entrada(input("Temperatura (°C): "), -50, 50, "Temperatura")
    N = validar_entrada(input("Nitrogênio (mg/kg): "), 0, 1000, "Nitrogênio")
    P = validar_entrada(input("Fósforo (mg/kg): "), 0, 1000, "Fósforo")
    K = validar_entrada(input("Potássio (mg/kg): "), 0, 1000, "Potássio")
    
    if incluir_fertilidade:
        fertilidade = int(input("Fertilidade (0 para baixa, 1 para alta): "))
        return pH, umidade, temperatura, N, P, K, fertilidade
    else:
        return pH, umidade, temperatura, N, P, K

def mostrar_grafico_fertilidade(fertilidade, pH, umidade, temperatura, N, P, K):
    categorias = ['pH', 'Umidade', 'Temperatura', 'N', 'P', 'K']
    valores = [pH, umidade, temperatura, N, P, K]
    
    plt.figure(figsize=(10, 6))
    plt.bar(categorias, valores, color=['blue', 'green', 'red', 'cyan', 'magenta', 'yellow'])
    plt.title(f"Análise do Solo - Fertilidade {'Alta' if fertilidade == 1 else 'Baixa'}")
    plt.xlabel("Parâmetros")
    plt.ylabel("Valores")
    
    for i, v in enumerate(valores):
        plt.text(i, v, f'{v:.2f}', ha='center', va='bottom')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    verificar_e_criar_tabela()
    service = AnaliseSoloService()

    while True:
        print("\nEscolha uma opção:")
        print("1 - Inserir dados manualmente")
        print("2 - Ler arquivo CSV")
        print("3 - Estimar fertilidade do solo")
        print("4 - Treinar modelo")
        print("5 - Sair")
        
        escolha = input("Digite o número da opção desejada: ")

        if escolha == '1':
            pH, umidade, temperatura, N, P, K, fertilidade = obter_entrada_usuario()
            service.salvar_analise(pH, umidade, temperatura, N, P, K, fertilidade)
            print("Dados inseridos com sucesso no banco de dados.")

        elif escolha == '2':
            caminho_csv = input("Digite o caminho do arquivo CSV: ")
            try:
                quantidade_processada = service.ler_e_salvar_csv(caminho_csv)
                print(f"Foram processadas e salvas {quantidade_processada} análises do arquivo CSV.")
            except Exception as e:
                print(f"Erro ao processar o arquivo CSV: {str(e)}")

        elif escolha == '3':
            try:
                pH, umidade, temperatura, N, P, K = obter_entrada_usuario(incluir_fertilidade=False)
                fertilidade = service.prever_fertilidade(pH, umidade, temperatura, N, P, K)
                print(f"A fertilidade prevista do solo é: {'Alta' if fertilidade == 1 else 'Baixa'}")
                
                mostrar_grafico_fertilidade(fertilidade, pH, umidade, temperatura, N, P, K)
            except ValueError as e:
                print(str(e))

        elif escolha == '4':
            print("Treinando o modelo...")
            if service.treinar_modelo():
                print("Modelo treinado com sucesso.")
            else:
                print("Falha ao treinar o modelo.")

        elif escolha == '5':
            print("Saindo do programa. Até logo!")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")