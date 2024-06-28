class Person:
  def __init__(self, name, surname, age):
    self.name = name
    self.surname = surname
    self.age = age
  
  def introduce_yourself(self):
    print(f"Hello! I'm {(self.name).capitalize()} {(self.surname).capitalize()} and I'm {self.age} years old.")

class Student(Person):
  def __init__(self, name, surname, age, university, degree):
    super().__init__(name, surname, age) #This method specifies the properties that the subclass will inherit from the superclass
    self.degree = degree
    self.university = university

  # def introduce_yourself(self):
  #   return super().introduce_yourself() 
  # This method will inherit the implementation of the superclass method. But we can define other behavior with the same method's name.

  def introduce_yourself(self):
    print(f"Hello! I'm {(self.name).capitalize()} {(self.surname).capitalize()} and I'm {self.age} years old and I'm studying {self.degree} in {self.university} University.")

person1 = Person('Jesse', 'Pinkman', 25)
student1 = Student('Walter', 'White', 19, 'California', 'Chemistry')

person1.introduce_yourself()
student1.introduce_yourself()