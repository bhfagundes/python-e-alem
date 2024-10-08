import cx_Oracle
from config.db_config import DBConfig
import logging

class OracleConnection:
    def __init__(self):
        self.dsn = cx_Oracle.makedsn(DBConfig.HOST, DBConfig.PORT, sid=DBConfig.SID)
        self.connection = None

    def connect(self):
        try:
            self.connection = cx_Oracle.connect(DBConfig.USERNAME, DBConfig.PASSWORD, self.dsn)
            logging.info("Conexão estabelecida com sucesso!")
            return self.connection
        except cx_Oracle.DatabaseError as e:
            logging.error(f"Erro ao conectar ao banco de dados: {e}")
            raise

    def close(self):
        if self.connection:
            try:
                self.connection.close()
                logging.info("Conexão fechada com sucesso!")
            except cx_Oracle.DatabaseError as e:
                logging.error(f"Erro ao fechar a conexão com o banco de dados: {e}")
                raise

    def __enter__(self):
        return self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()