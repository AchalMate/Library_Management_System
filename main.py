from book import BookManager,Book,EBook,AudioBook
from user import UserManager,Person,User
from checkout import CheckoutManager
import storage

class Library:
    def __init__(self):
        self.book_manager = BookManager()
        self.user_manager = UserManager()
        self.checkout_manager = CheckoutManager(self.book_manager)

    def main_menu(self):
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. List Books")
        print("3. Add User")
        print("4. List Users")
        print("5. Checkout Book")
        print("6. Checkin Book")
        print("7. Search Book")
        print("8. Update Book")
        print("9. Delete Book")
        print("10. Exit")
        choice = input("Enter choice: ")
        return choice

    def run(self):
        while True:
            choice = self.main_menu()
            if choice == '1':
                title = input("Enter title: ")
                author = input("Enter author: ")
                isbn = input("Enter ISBN: ")
                book_type = input("Enter book type (regular/ebook/audiobook): ").lower()
                if book_type == "ebook":
                    file_format = input("Enter file format: ")
                    book = EBook(title, author, isbn, file_format)
                elif book_type == "audiobook":
                    duration = int(input("Enter duration in minutes: "))
                    book = AudioBook(title, author, isbn, duration)
                else:
                    book = Book(title, author, isbn,book_type)
                self.book_manager.add_book(book)
                print("Book added.")
            elif choice == '2':
                self.book_manager.list_books()
            elif choice == '3':
                name = input("Enter user name: ")
                user_id = input("Enter user ID: ")
                user = User(name, user_id)
                self.user_manager.add_user(user)
                print("User added.")
            elif choice == '4':
                self.user_manager.list_users()
            elif choice == '5':
                user_id = input("Enter user ID: ")
                isbn = input("Enter ISBN of the book to checkout: ")
                if self.checkout_manager.checkout_book(user_id, isbn):
                    print("Book checked out.")
                else:
                    print("Book is not available or does not exist.")
            elif choice == '6':
                user_id = input("Enter user ID: ")
                isbn = input("Enter ISBN of the book to checkin: ")
                if self.checkout_manager.checkin_book(user_id, isbn):
                    print("Book checked in.")
                else:
                    print("Book was not checked out or does not exist.")
            elif choice == '7':
                attribute = input("Enter attribute to search by (title, author, isbn): ")
                value = input(f"Enter value for {attribute}: ")
                results = self.book_manager.search_book(**{attribute: value})
                if results:
                    for book in results:
                        print(book)
                else:
                    print("No books found.")
            elif choice == '8':
                isbn = input("Enter ISBN of the book to update: ")
                attribute = input("Enter attribute to update (title, author, file_format, duration): ")
                value = input(f"Enter new value for {attribute}: ")
                if attribute == "duration":
                    value = int(value)
                if self.book_manager.update_book(isbn, **{attribute: value}):
                    print("Book updated.")
                else:
                    print("Book not found.")
            elif choice == '9':
                isbn = input("Enter ISBN of the book to delete: ")
                if self.book_manager.delete_book(isbn):
                    print("Book deleted.")
                else:
                    print("Book not found.")
            elif choice == '10':
                print("Exiting.")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    library = Library()
    library.run()
