from abc import ABC, abstractmethod
import json
import uuid
class Item(ABC):
    def __init__(self, title, author, price):
        self.__id = title + "-" + str(uuid.uuid4())
        self.__title = title
        self.__author = author
        self.__price = price

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

    def save_to_database(self, db, table_name):
        data = {
            "id": self.__id,
            "title": self.get_title(),
            "author": self.get_author(),
            "price": self.get_price(),
        }
        serilized_data = json.dumps(data)
        db.insert(table_name, self.get_id(), serilized_data)

    def search_item(self, search_term):
        results = []
        for table_name in ['books', 'magazine', 'dvd']:
            self.cursor.execute(f"SELECT key, value FROM {table_name} WHERE key LIKE ? OR value LIKE ?", ('%' + search_term + '%', '%' + search_term + '%'))
            rows = self.cursor.fetchall()
            for row in rows:
                try:
                    item_data = json.loads(row[1])
                    if not isinstance(item_data, dict):
                        item_data = {'data': row[1]}  # Create a new dictionary and copy relevant data
                    item_data['type'] = table_name.capitalize()
                    results.append((row[0], item_data))
                except (json.JSONDecodeError, KeyError):
                    continue
        return results


    @abstractmethod
    def details(self):
        pass
