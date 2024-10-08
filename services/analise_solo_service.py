import pandas as pd
from repositories.analise_solo_repository import AnaliseSoloRepository
from models.analise_solo import AnaliseSolo

class AnaliseSoloService:
    def __init__(self):
        self.repository = AnaliseSoloRepository()

    def salvar_analise(self, pH, umidade, temperatura, N, P, K, fertilidade):
        analise_solo = AnaliseSolo(pH, umidade, temperatura, N, P, K, fertilidade)
        self.repository.salvar(analise_solo)

    def ler_csv(self, csv_file_path):
        df = pd.read_csv(csv_file_path)
        data = list(df.itertuples(index=False, name=None))
        return data

    def salvar_analise_em_lote(self, csv_file_path):
        data = self.ler_csv(csv_file_path)
        self.repository.bulk_insert(data)

    def salvar_multiplas_analises(self, analises):
        self.repository.salvar_multiplas_analises(analises)