from Book import Book
from Member import Member
from Library import Library

library = Library()
staff = Member("Chumbita Luciano", 1)
book1 = Book("La sombra del viento", "No se", 1111)
book2 = Book("Hábitos Atómicos", "No sé", 2222)
library.register_member(staff)
library.add_book(book1)
library.add_book(book2)

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
  member_id = int(input("Member id: "))
  book_isbn = int(input("Book ISBN: "))

  library.borrow_book(member_id, book_isbn)

def return_book():
  print("-----|RETURN A BOOK|-----")
  member_id = input("Member id: ")
  book_isbn = input("Book ISBN: ")
  f_book = False
  f_member = False

  for m in library.members:
    if m.id == member_id:
      member = m
      f_member = True
      for b in m.borrowed_books:
        if b.isbn == book_isbn:
          book = b
          f_book = True
          break
      break

  if f_member and f_book:
    member.return_book(book)
    print(f"The book {book} was returned successfully")
  elif f_member == False:
    print(f'Member id "{member_id}" was not found.')
  elif f_book == False:
    print(f'The book with ISBN "{book_isbn}" was not found.')

def borrowed_books():
  print(f"-----|BORROWED BOOKS|-----\n{'Books':<50} {'Member':<15}")
  for m in library.members:
    for b in m.borrowed_books:
      print(f"{b} {m}")
  

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
    
    input("Press ENTER to continue...")

if __name__ == "__main__":
  main()