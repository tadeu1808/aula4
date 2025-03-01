import _mysql_connector
from config import Config

class ProduoModel:
    
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
        
    def get_all_products(self):
        query = "SELECT id, nome, preco FROM produtos"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def insert_product(self, nome, preco):
        query = "INSERT INTO produtos (nome, preco) VALUES (%s, %s)"
        
        self.cursor.execute(query,(nome, preco))
        self.connection.commit()
        return self.cursor.lastrowid
    
    def get_product_by_id(self, product_id):
        query = "SELECT id, nome, preco FROM produtos WHERE id = %s"
        self.cursor.execute(query, product_id)
        return self.cursor.fetchone()
    def delete_product_by_id(self, product_id):
        query = "DELETE FROM produtos WHERE id = %s"
        self.cursor.execute(query, product_id)
        return self.cursor.rowcount
    
    
    
    
        