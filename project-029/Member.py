class Member():
  def __init__(self, name, id_member):
    self.name = name
    self.id = id_member
    self.borrowed_books = []

  def __str__(self):
    return f"{(self.name).capitalize()}"
  
  def add_book(self, book):
    self.borrowed_books.append(book)
  
  def return_book(self, book):
    self.borrowed_books.remove(book)