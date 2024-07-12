from Book import Book
from Member import Member

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.libros.append(book)

    def register_member(self, member):
        self.members.append(member)
    
    def borrow_book(self, id_member, isbn):
        for member in self.members:
            if member.id == id_member:
                for book in self.books:
                    if book.isbn == isbn and book.availability:
                        member.add_book(book)
                        book.availability = False
                    else: 
                        print(f"The requested book is not available")
            else: 
                print("You are not registered as a member of the library")