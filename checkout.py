import storage

class CheckoutManager:
    def __init__(self, book_manager, storage_file='checkouts.json'):
        self.book_manager = book_manager
        self.storage_file = storage_file
        self.checkouts = self.load_checkouts()

    def load_checkouts(self):
        return storage.load_data(self.storage_file)

    def save_checkouts(self):
        storage.save_data(self.checkouts, self.storage_file)

    def checkout_book(self, user_id, isbn):
        for book in self.book_manager.books:
            if book.isbn == isbn and book.available:
                book.available = False
                self.checkouts.append({"user_id": user_id, "isbn": isbn})
                self.save_checkouts()
                self.book_manager.save_books()
                return True
        return False

    def checkin_book(self, user_id, isbn):
        for checkout in self.checkouts:
            if checkout["user_id"] == user_id and checkout["isbn"] == isbn:
                self.checkouts.remove(checkout)
                for book in self.book_manager.books:
                    if book.isbn == isbn:
                        book.available = True
                        self.save_checkouts()
                        self.book_manager.save_books()
                        return True
        return False
