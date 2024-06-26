import storage
import json
class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available: {self.available}"

class EBook(Book):
    def __init__(self, title, author, isbn, file_format, available=True, **kwargs):
        super().__init__(title, author, isbn, available)
        self.file_format = file_format

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available: {self.available}, File Format: {self.file_format}"

class AudioBook(Book):
    def __init__(self, title, author, isbn, duration, available=True, **kwargs):
        super().__init__(title, author, isbn, available)
        self.duration = duration

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available: {self.available}, Duration: {self.duration} minutes"
class BookManager:
    def __init__(self, storage_file='books.json'):
        self.storage_file = storage_file
        self.books = self.load_books()

    def load_books(self):
        books_data = storage.load_data(self.storage_file)
        books = []
        for data in books_data:
            if 'file_format' in data:
                books.append(EBook(**data))
            elif 'duration' in data:
                books.append(AudioBook(**data))
            else:
                books.append(Book(**data))
        return books

    def save_books(self):
        books_data = [book.__dict__ for book in self.books]
        storage.save_data(books_data, self.storage_file)

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def list_books(self):
        for book in self.books:
            print(book)

    def search_book(self, **kwargs):
        results = []
        for book in self.books:
            match = True
            for key, value in kwargs.items():
                if getattr(book, key) != value:
                    match = False
                    break
            if match:
                results.append(book)
        return results

    def update_book(self, isbn, **kwargs):
        for book in self.books:
            if book.isbn == isbn:
                for key, value in kwargs.items():
                    setattr(book, key, value)
                self.save_books()
                return True
        return False

    def delete_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                self.save_books()
                return True
        return False
