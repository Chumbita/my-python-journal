from Book import Book
from Member import Member
from Library import Library

library = Library()

def register_member():
  print("-----|REGISTRATION|-----\n")
  member_name = input("Enter your name: ")
  id_member = ((library.members[-1]).id) + 1
  new_member = Member(member_name, id_member)
  library.register_member(new_member)
  print(f"----|MEMBER REGISTERED SUCCESSFULLY|-----\nMember name: {new_member.name}\nMember id: {new_member.id}")

def find_book():
  flag = True
  print("-----|FIND A BOOK|-----\n1)Find a book by name.\n2)Find a book by ISBN.")
  user_option = int(input("Choose an operation: "))
  if user_option == 1:
    book = input("Book's Name: ")
    for b in library.books:
      if (b.title).lower() == book.lower():
        print(f"Book: {(b.title).upper()}\nAutor: {b.autor}\nISBN: {b.isbn}\nAvailability: {b.availability}")
        break
      else: 
        print("We couldn't find the book by the title, try with the other opcion.")
  elif user_option == 2:
    book = input("Book's ISBN: ")
    for b in library.books:
      if b.isbn == book:
        print(f"Book: {(b.title).upper()}\nAutor: {b.autor}\nISBN: {b.isbn}\nAvailability: {b.availability}")
        break
      else: 
        print("We couldn't find the book by the ISBN, try with the other opcion ")
  else: 
    print("Invalid option.")
  
def borrow_book():
  print("-----|REQUEST BOOK LOAN|----\n")
  member_id = input("Member id: ")
  book_isbn = input("Book ISBN: ")

  library.borrow_book(member_id, book_isbn)


def main():
  flag = True
  while flag:
    print("-----|BOOKS FOR EVERYONE|-----\n1)Register as a member.\n2)Find a book.\n3)Borrow a book.\n4)Return a book.\n5)Borrowed books.\n6)Exit.\n")
    user_option = int(input("Choose an operation: "))
    if user_option == 1:
      register_member()
    elif user_option == 2:
      find_book()
    elif user_option == 3:
      borrow_book()
    elif user_option == 4:
      return_book()
    elif user_option == 5:
      borrowed_books()
    elif user_option == 6:
      flag = False
    else:
      print("Invalid option.")