import mysql.connector
from config import Config

class UsuarioModel:
    
    def __init__(self):
        self.config = Config()
        #iniciando a configuração
        self.connection = mysql.connector.connect(
            host=self.config.MYSQL_HOST,
            user=self.config.MYSQL_USER,
            password=self.config.MYSQL_PASSWORD,
            database=self.config.MYSQL_DB                               
        )
        
        #cursor - traz o resultado em  dicionarios
        
        self.cursor = self.connection.cursor(dictionary=True)
        
    def get_all_users(self):
        query = "SELECT id, email, nome, idade FROM usuarios"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def insert_user(self, email, nome, idade):
        query = "INSERT INTO usuarios (email, nome, idade) VALUES (%s, %s, %s)"
        self.cursor.execute(query,(email, nome, idade))
        self.connection.commit()
        return self.cursor.lastrowid
    
    def get_user_by_id(self, user_id):
        query = "SELECT email, nome, idade FROM usuarios WHERE id = %s"
        self.cursor.execute(query, user_id)
        return self.cursor.fetchone()
    
    #def delete_user_by_id(self, user_id):
    #    query = "DELETE FROM usuarios WHERE id = %s"
    #    self.cursor.execute(query, user_id)
    #    self.connection.commit()
    #    return self.cursor.rowcount
    
    def update_user_by_id(self, user_id, nome, idade, email):
        query = "UPDATE usuarios SET email = %s, nome = %s, idade = %s WHERE id = %s"
        self.cursor.execute(query, (email, nome, idade, user_id))
        self.connection.commit()
        return self.cursor.rowcount
    
    def close_connection(self):
        self.cursor.close()
        self.connection.close()