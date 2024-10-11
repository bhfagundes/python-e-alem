from db.connection import OracleConnection

class AnaliseSoloRepository:
    def salvar(self, pH, umidade, temperatura, N, P, K, fertilidade):
        with OracleConnection() as connection:
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO analise_solo (pH, umidade, temperatura, N, P, K, fertilidade)
                VALUES (:1, :2, :3, :4, :5, :6, :7)
            """, (pH, umidade, temperatura, N, P, K, fertilidade))
            connection.commit()

    def salvar_em_lote(self, dados):
        with OracleConnection() as connection:
            cursor = connection.cursor()
            cursor.executemany("""
                INSERT INTO analise_solo (pH, umidade, temperatura, N, P, K, fertilidade)
                VALUES (:1, :2, :3, :4, :5, :6, :7)
            """, dados)
            connection.commit()

    def obter_todos_dados(self):
        with OracleConnection() as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT pH, umidade, temperatura, N, P, K, fertilidade FROM analise_solo')
            return cursor.fetchall()