from Book import Book
from Member import Member
from Library import Library
import os 

library = Library()
staff = Member("Tomás Casals", 1)
book1 = Book("The Shadow of the Wind", "Carlos Ruiz Zafón", "1111")
book2 = Book("Atomic Habits", "James Clear", "2222")
library.register_member(staff)
library.add_book(book1)
library.add_book(book2)

def register_member():
  print("-----|REGISTRATION|-----\n")
  member_name = input("Enter your name: ")
  member_id = ((library.members[-1]).id) + 1
  new_member = Member(member_name, member_id)
  library.register_member(new_member)
  os.system("cls")
  print(f"----|MEMBER REGISTERED SUCCESSFULLY|-----\nMember name: {new_member.name}\nMember id: {new_member.id}")

def find_book():
  op_flag = False
  print("-----|FIND A BOOK|-----\n1)Find a book by name.\n2)Find a book by ISBN.")
  user_option = int(input("\nChoose an operation: "))
  os.system("cls")

  if user_option == 1:
    print("-----|FIND A BOOK|-----")
    book = input("Book's Name: ")
    for b in library.books:
      if (b.title).lower() == book.lower():
        print(f"\nBOOK: {(b.title).upper()}\nAUTOR: {b.autor}\nISBN: {b.isbn}\nAVAILABILITY: {b.availability}")
        op_flag = True
        break
  elif user_option == 2:
    print("-----|FIND A BOOK|-----")
    book = input("Book's ISBN: ")
    for b in library.books:
      if b.isbn == book:
        print(f"\nBOOK: {(b.title).upper()}\nAUTOR: {b.autor}\nISBN: {b.isbn}\nAVAILABILITY: {b.availability}")
        op_flag = True
        break
  else: 
    print("\nInvalid option.")
  
  if not op_flag: print("\nWe couldn't found the book")
  
def borrow_book():
  print("-----|REQUEST BOOK LOAN|----")
  member_id = int(input("Member id: "))
  book_isbn = input("Book ISBN: ")

  library.borrow_book(member_id, book_isbn)

def return_book():
  print("-----|RETURN A BOOK|-----")
  member_id = int(input("Member id: "))
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
    book.availability = True
    print(f"\nThe book {book} was returned successfully")
  elif f_member == False:
    print(f'\nMember id "{member_id}" was not found.')
  elif f_book == False:
    print(f'\nThe book with ISBN "{book_isbn}" was not found.')

def borrowed_books():
  print(f"-----|BORROWED BOOKS|-----\n{'Books':<50} {'Member':<15}")
  for m in library.members:
    for b in m.borrowed_books:
      print(f"{(f'{b.title.upper()} - {b.autor}'):<50} {m}")
  

def main():
  flag = True
  while flag:
    print("-----|BOOKS FOR EVERYONE|-----\n1)Register as a member.\n2)Find a book.\n3)Borrow a book.\n4)Return a book.\n5)Borrowed books.\n6)Exit.\n")
    user_option = int(input("Choose an operation: "))
    os.system("cls")
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
    
    input("\nPress ENTER to continue...")
    os.system("cls")

if __name__ == "__main__":
  main()