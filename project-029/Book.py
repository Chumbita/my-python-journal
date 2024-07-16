class Book():
  def __init__(self, title, autor, isbn):
    self.title = title
    self.autor = autor
    self.isbn = isbn
    self.availability = True

  def __str__(self):
    return f"{self.title} por {self.autor} (ISBN: {self.isbn})"
