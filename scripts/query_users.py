from db.connection import OracleConnection
from repositories.user_repository import UserRepository
from services.user_service import UserService

def query_users():
    connection = OracleConnection()
    try:
        conn = connection.connect()
        print("Conexão estabelecida com sucesso!")

        user_repository = UserRepository(conn)
        user_service = UserService(user_repository)

        users = user_service.get_all_users()
        for user in users:
            print(user)

    except cx_Oracle.DatabaseError as e:
        print(f"Erro ao conectar ao banco de dados: {e}")

    finally:
        connection.close()