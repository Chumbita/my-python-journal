class Member():
  def __init__(self, name, id_member):
    self.name = name
    self.id = id_member
    self.borrowed_books = []
  
  def add_book(self, book):
    self.borrowed_books.append(book)
  
  def return_book(self, book):
    self.borrowed_books.remove(book)