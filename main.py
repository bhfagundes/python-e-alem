import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import seaborn as sns
import matplotlib.pyplot as plt
from services.analise_solo_service import AnaliseSoloService
from migrations.migration import verificar_e_criar_tabela
from scripts.query_users import query_users
from models.analise_solo import AnaliseSolo

# Função para prever a fertilidade do solo
def prever_fertilidade(pH, umidade, temperatura, N, P, K, scaler, model):
    input_data = [[pH, umidade, temperatura, N, P, K]]
    input_data = scaler.transform(input_data)
    prediction = model.predict(input_data)
    return int(prediction[0])

if __name__ == "__main__":
    # Executar a função query_users
    #query_users()

    # Verificar e criar tabela se necessário
    verificar_e_criar_tabela()

    # Passo 1: Coleta de Dados
    data = {
        'pH': [6.5, 7.0, 5.5, 6.0, 6.8, 7.2, 5.8, 6.3],
        'umidade': [30, 45, 50, 35, 40, 55, 60, 33],
        'temperatura': [20, 22, 19, 21, 23, 18, 17, 22],
        'N': [10, 20, 15, 25, 18, 22, 14, 19],
        'P': [5, 10, 7, 12, 8, 11, 6, 9],
        'K': [8, 15, 10, 20, 13, 17, 9, 14],
        'fertilidade': [1, 0, 1, 0, 1, 0, 1, 0]  
    }

    df = pd.DataFrame(data)

    # Passo 2: Pré-processamento de Dados
    X = df.drop('fertilidade', axis=1)
    y = df['fertilidade']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Passo 3: Análise Exploratória de Dados (EDA)
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.show()

    # Passo 4: Desenvolvimento de Modelos de Aprendizado de Máquina
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Passo 5: Avaliação do Modelo
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))

    # Exemplo de uso da função de previsão
    pH = 6.5
    umidade = 30
    temperatura = 20
    N = 10
    P = 5
    K = 8

    fertilidade = prever_fertilidade(pH, umidade, temperatura, N, P, K, scaler, model)
    print(f"A fertilidade prevista do solo é: {'Alta' if fertilidade == 1 else 'Baixa'}")

    # Salvar dados no banco de dados
    service = AnaliseSoloService()
    for i in range(len(df)):
        service.salvar_analise(df.iloc[i]['pH'], df.iloc[i]['umidade'], df.iloc[i]['temperatura'], df.iloc[i]['N'], df.iloc[i]['P'], df.iloc[i]['K'], df.iloc[i]['fertilidade'])

    # Salvar dados em lote a partir de um arquivo CSV
    #csv_file_path = 'path/to/your/csvfile.csv'
    #service.salvar_analise_em_lote(csv_file_path)

    # Salvar múltiplas análises
    #analises = [AnaliseSolo(row.pH, row.umidade, row.temperatura, row.N, row.P, row.K, row.fertilidade) for row in df.itertuples(index=False)]
    #service.salvar_multiplas_analises(analises)