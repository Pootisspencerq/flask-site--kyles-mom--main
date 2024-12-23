import sqlite3

class DatabaseManager:
    def __init__(self, dbname):
        self.conn = None
        self.cursor = None
        self.dbname = dbname

    def open(self):
        self.conn = sqlite3.connect(self.dbname)
        self.cursor = self.conn.cursor()
    
    def close(self):
        self.cursor.close()
        self.conn.close()

    def get_all_articles(self):
        self.open()
        self.cursor.execute("""SELECT * FROM articles""")
        data = self.cursor.fetchall()
        self.close()
        return data
    
    def get_article(self, article_id):
        self.open()
        self.cursor.execute("""SELECT * FROM articles WHERE id=?""", [article_id])
        data = self.cursor.fetchone()
        self.close()
        return data

    def get_all_categories(self):
        self.open()
        self.cursor.execute("""SELECT * FROM categories """)
        data = self.cursor.fetchall()
        self.close()
        return data
    
    def get_category_articles(self, category_id):
        self.open()
        self.cursor.execute("""SELECT * FROM articles WHERE category_id=? """,[category_id])
        data = self.cursor.fetchall()
        self.close()
        return data
    
    def add_article(self, title, content, image, user_id, category_id):
        self.open()
        self.cursor.execute("""INSERT INTO articles (title, content, image, user_id, category_id) VALUES(?,?,?,?,?)""",
[title, content, image, user_id, int(category_id)])
        
        self.conn.commit()
        self.close()
        return 