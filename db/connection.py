import cx_Oracle
from config.db_config import DBConfig

class OracleConnection:
    def __init__(self):
        self.dsn = cx_Oracle.makedsn(DBConfig.HOST, DBConfig.PORT, sid=DBConfig.SID)
        self.connection = None

    def connect(self):
        self.connection = cx_Oracle.connect(DBConfig.USERNAME, DBConfig.PASSWORD, self.dsn)
        return self.connection

    def close(self):
        if self.connection:
            self.connection.close()