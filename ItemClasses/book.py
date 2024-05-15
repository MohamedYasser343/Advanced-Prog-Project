import json
from ItemClasses.item import Item
# from sqlite3 import OperationalError

class Book(Item):
    def __init__(self, title, author, price, isbn, genre, num_pages):
        super().__init__(title, author, price)
        self.__isbn = isbn
        self.__genre = genre
        self.__num_pages = num_pages

    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, isbn):
        self.__isbn = isbn

    def get_genre(self):
        return self.__genre

    def set_genre(self, genre):
        self.__genre = genre

    def get_num_pages(self):
        return self.__num_pages

    def set_num_pages(self, num_pages):
        self.__num_pages = num_pages

    def save_to_database(self, db, table_name):
        data = {
            "id": self.get_id(),
            "title": self.get_title(),
            "author": self.get_author(),
            "price": self.get_price(),
            "isbn": self.get_isbn(),
            "genre": self.get_genre(),
            "num_pages": self.get_num_pages()
        }
        serilized_data = json.dumps(data)
        db.insert(table_name, self.get_id(), serilized_data)

    def details(self):
        return f"Title: {self.get_title()}\nAuthor: {self.get_author()}\nPrice: {self.get_price()}\nISBN: {self.get_isbn()}\nGenre: {self.get_genre()}\nNumber of pages: {self.get_num_pages()}"
