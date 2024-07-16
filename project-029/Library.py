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
        f_member = False
        f_book = False

        for member in self.members:
            if member.id == id_member:
                f_member = True
                for book in self.books:
                    if book.isbn == isbn and book.availability:
                        f_book = True
                        member.add_book(book)
                        book.availability = False
                        print("\nPetition successfully approved")
                        break
                break
        
        if f_member == False: print(f'\nThe member with id "{id_member}" was not found.')
        elif f_book == False: print(f'\nThe book with ISBN "{isbn}" was not found.')
