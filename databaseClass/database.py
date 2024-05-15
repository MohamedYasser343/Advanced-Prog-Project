import sqlite3
import json

class Database:
    def __init__(self, filename="data.db"):
        self.filename = filename
        self.conn = sqlite3.connect(filename)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name):
        self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name} (
                                key TEXT PRIMARY KEY,
                                value TEXT)''')
        self.conn.commit()

    def insert(self, table_name, key, value):
        self.cursor.execute(f"INSERT INTO {table_name} (key, value) VALUES (?, ?)", (key, json.dumps(value)))
        self.conn.commit()

    def remove(self, table_name, key):
        self.cursor.execute(f"DELETE FROM {table_name} WHERE key=?", (key,))
        self.conn.commit()

    def get(self, table_name, key):
        self.cursor.execute(f"SELECT value FROM {table_name} WHERE key=?", (key,))
        row = self.cursor.fetchone()
        return json.loads(row[0]) if row else None

    def contains(self, table_name, key):
        self.cursor.execute(f"SELECT EXISTS(SELECT 1 FROM {table_name} WHERE key=?)", (key,))
        return self.cursor.fetchone()[0] == 1

    def keys(self, table_name):
        self.cursor.execute(f"SELECT key FROM {table_name}")
        return [row[0] for row in self.cursor.fetchall()]

    def values(self, table_name):
        self.cursor.execute(f"SELECT value FROM {table_name}")
        return [json.loads(row[0]) for row in self.cursor.fetchall()]

    def items(self, table_name):
        self.cursor.execute(f"SELECT key, value FROM {table_name}")
        return [(row[0], json.loads(row[1])) for row in self.cursor.fetchall()]
    
    def search(self, table_name, search_term):
        self.cursor.execute(f"SELECT key, value FROM {table_name} WHERE key LIKE ? OR value LIKE ?", ('%' + search_term + '%', '%' + search_term + '%'))
        return [(row[0], json.loads(row[1])) for row in self.cursor.fetchall()]
    
    def close(self):
        self.conn.close()
