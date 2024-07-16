from Book import Book
from Member import Member

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)
    
    def borrow_book(self, id_member, isbn):
        for member in self.members:
            if member.id == id_member:
                for book in self.books:
                    if book.isbn == isbn:
                        member.add_book(book)
                        book.availability = False
                        print("Petition successfully approved")
                        break
                    else: 
                        print(f"The requested book is not available")
                break
            else: 
                print("You are not registered as a member of the library")
    