import json
from ItemClasses.item import Item

class DVD(Item):
    def __init__(self, title, author, price, director, duration, genre):
        super().__init__(title, author, price)
        self.__director = director
        self.__duration = duration
        self.__genre = genre

    def get_director(self):
        return self.__director

    def set_director(self, director):
        self.__director = director

    def get_duration(self):
        return self.__duration

    def set_duration(self, duration):
        self.__duration = duration

    def get_genre(self):
        return self.__genre

    def set_genre(self, genre):
        self.__genre = genre
    
    def save_to_database(self, db, table_name):
        data = {
            "id": self._Item__id,
            "title": self.get_title(),
            "author": self.get_author(),
            "price": self.get_price(),
            "director": self.get_director(),
            "duration": self.get_duration(),
            "genre": self.get_genre(),
        }
        serilized_data = json.dumps(data)
        db.insert(table_name, self.get_id(), serilized_data)
    
    def details(self):
        return f"Title: {self.get_title()}\nAuthor: {self.get_author()}\nPrice: {self.get_price()}\nDirector: {self.get_director()}\nDuration: {self.get_duration()}\nGenre: {self.get_genre()}"
