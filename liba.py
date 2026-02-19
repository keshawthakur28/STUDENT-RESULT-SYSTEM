class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.is_borrowed = False

    def __str__(self):
        return f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Borrowed: {self.is_borrowed}"


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.is_borrowed = True
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"Sorry, '{book.title}' is already borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} hasn't borrowed '{book.title}'.")

    def display_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name}'s borrowed books:")
            for book in self.borrowed_books:
                print(f" - {book.title}")
        else:
            print(f"{self.name} has no borrowed books.")


class Staff(Member):
    def __init__(self, member_id, name, staff_id):
        super().__init__(member_id, name)
        self.staff_id = staff_id

    def add_book(self, library, book):
        library.add_book(book)
        print(f"{self.name} added the book '{book.title}' to the library.")

    def remove_book(self, library, book):
        library.remove_book(book)
        print(f"{self.name} removed the book '{book.title}' from the library.")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            print(f"The book '{book.title}' does not exist in the library.")

    def display_books(self):
        if self.books:
            print("Books available in the library:")
            for book in self.books:
                print(f" - {book.title} by {book.author}")
        else:
            print("No books available in the library.")


if __name__ == "__main__":

    library = Library()

    staff1 = Staff("S001", "Alice", "STAFF001")
    staff2 = Staff("S002", "Bob", "STAFF002")

    book1 = Book("To Kill a Mockingbird", "Harper Lee", "B001")
    book2 = Book("1984", "George Orwell", "B002")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "B003")

    staff1.add_book(library, book1)
    staff1.add_book(library, book2)
    staff2.add_book(library, book3)

    library.display_books()

    member1 = Member("M001", "John")
    member2 = Member("M002", "Sarah")

    member1.borrow_book(book1)
    member2.borrow_book(book2)

    member1.display_borrowed_books()
    member2.display_borrowed_books()

    member1.return_book(book1)
    member2.return_book(book2)

    library.display_books()

    staff1.remove_book(library, book3)
    library.display_books()
