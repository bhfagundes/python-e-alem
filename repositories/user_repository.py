class UserRepository:
    def __init__(self, connection):
        self.connection = connection

    def get_all_users(self):
        cursor = self.connection.cursor()
        cursor.execute(f"ALTER SESSION SET CURRENT_SCHEMA = {DBConfig.SCHEMA}")
        cursor.execute("SELECT * FROM usuarios")
        users = cursor.fetchall()
        cursor.close()
        return users