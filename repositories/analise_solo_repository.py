from db.connection import OracleConnection
from models.analise_solo import AnaliseSolo

class AnaliseSoloRepository:
    def salvar(self, analise_solo):
        with OracleConnection() as connection:
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO analise_solo (pH, umidade, temperatura, N, P, K, fertilidade)
                VALUES (:1, :2, :3, :4, :5, :6, :7)
            """, (analise_solo.pH, analise_solo.umidade, analise_solo.temperatura, analise_solo.N, analise_solo.P, analise_solo.K, analise_solo.fertilidade))
            connection.commit()
            cursor.close()

    def salvar_multiplas_analises(self, analises):
        data = [(analise.pH, analise.umidade, analise.temperatura, analise.N, analise.P, analise.K, analise.fertilidade) for analise in analises]
        with OracleConnection() as connection:
            cursor = connection.cursor()
            cursor.executemany("""
                INSERT INTO analise_solo (pH, umidade, temperatura, N, P, K, fertilidade)
                VALUES (:1, :2, :3, :4, :5, :6, :7)
            """, data)
            connection.commit()
            cursor.close()

    def bulk_insert(self, data):
        with OracleConnection() as connection:
            cursor = connection.cursor()
            cursor.executemany("""
                INSERT INTO analise_solo (pH, umidade, temperatura, N, P, K, fertilidade)
                VALUES (:1, :2, :3, :4, :5, :6, :7)
            """, data)
            connection.commit()
            cursor.close()