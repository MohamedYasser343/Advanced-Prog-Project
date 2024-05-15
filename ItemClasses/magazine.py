import json
from ItemClasses.item import Item

class Magazine(Item):
    def __init__(self, title, author, price, issue_number, publication_date, editor):
        super().__init__(title, author, price)
        self.__issue_number = issue_number
        self.__publication_date = publication_date
        self.__editor = editor

    def get_issue_number(self):
        return self.__issue_number

    def set_issue_number(self, issue_number):
        self.__issue_number = issue_number

    def get_publication_date(self):
        return self.__publication_date

    def set_publication_date(self, publication_date):
        self.__publication_date = publication_date

    def get_editor(self):
        return self.__editor

    def set_editor(self, editor):
        self.__editor = editor

    def save_to_database(self, db, table_name):
        data = {
            "id": self._Item__id,
            "title": self.get_title(),
            "author": self.get_author(),
            "price": self.get_price(),
            "issue_number": self.get_issue_number(),
            "publication_date": self.get_publication_date(),
            "editor": self.get_editor(),
        }
        serilized_data = json.dumps(data)
        db.insert(table_name, self.get_id(), serilized_data)

    def details(self):
        return f"Title: {self.get_title()}\nAuthor: {self.get_author()}\nPrice: {self.get_price()}\nIssue number: {self.get_issue_number()}\nPublication date: {self.get_publication_date()}\nEditor: {self.get_editor()}"
    