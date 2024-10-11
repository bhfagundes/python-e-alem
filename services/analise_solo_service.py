import joblib
import pandas as pd
import csv
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from repositories.analise_solo_repository import AnaliseSoloRepository

class AnaliseSoloService:
    def __init__(self):
        self.repository = AnaliseSoloRepository()
        self.scaler = None
        self.model = None
        self.carregar_modelo()

    def carregar_modelo(self):
        try:
            self.scaler = joblib.load('scaler_fertilidade.joblib')
            self.model = joblib.load('modelo_fertilidade.joblib')
        except FileNotFoundError:
            print("Modelo não encontrado. Por favor, treine o modelo primeiro.")

    def treinar_modelo(self):
        dados = self.repository.obter_todos_dados()
        if not dados:
            print("Não há dados suficientes para treinar o modelo.")
            return False

        df = pd.DataFrame(dados, columns=['pH', 'umidade', 'temperatura', 'N', 'P', 'K', 'fertilidade'])
        X = df[['pH', 'umidade', 'temperatura', 'N', 'P', 'K']]
        y = df['fertilidade']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        self.scaler = StandardScaler()
        X_train_scaled = self.scaler.fit_transform(X_train)

        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(X_train_scaled, y_train)

        joblib.dump(self.scaler, 'scaler_fertilidade.joblib')
        joblib.dump(self.model, 'modelo_fertilidade.joblib')

        print("Modelo treinado e salvo com sucesso.")
        return True

    def prever_fertilidade(self, pH, umidade, temperatura, N, P, K):
        if self.model is None or self.scaler is None:
            raise ValueError("Modelo não carregado. Por favor, treine o modelo primeiro.")
        
        # Criar um DataFrame com os nomes das colunas
        input_data = pd.DataFrame([[pH, umidade, temperatura, N, P, K]], 
                                  columns=['pH', 'umidade', 'temperatura', 'N', 'P', 'K'])
        
        # Aplicar o scaler
        input_data_scaled = self.scaler.transform(input_data)
        
        # Fazer a previsão
        prediction = self.model.predict(input_data_scaled)
        return int(prediction[0])

    def salvar_analise(self, pH, umidade, temperatura, N, P, K, fertilidade):
        self.repository.salvar(pH, umidade, temperatura, N, P, K, fertilidade)

    def ler_e_salvar_csv(self, caminho_arquivo):
        dados = []
        with open(caminho_arquivo, 'r') as arquivo:
            leitor_csv = csv.DictReader(arquivo)
            for linha in leitor_csv:
                try:
                    pH = float(linha['pH'])
                    umidade = float(linha['umidade'])
                    temperatura = float(linha['temperatura'])
                    N = float(linha['N'])
                    P = float(linha['P'])
                    K = float(linha['K'])
                    fertilidade = int(linha['fertilidade'])
                    dados.append([pH, umidade, temperatura, N, P, K, fertilidade])
                except ValueError as e:
                    print(f"Erro na linha {leitor_csv.line_num}: {str(e)}")
        
        if dados:
            self.repository.salvar_em_lote(dados)
        return len(dados)