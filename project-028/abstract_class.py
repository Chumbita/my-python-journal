from abc import ABC, abstractmethod

class Person(ABC):
  @abstractmethod
  def __init__(self, name, surname, age ):
    self.name = name
    self.surname = surname
    self.age = age 

  @abstractmethod
  def introduce(self):
    pass

class Student(Person):
  def __init__(self, name, surname, age, grade, university):
    super().__init__(name, surname, age)
    self.grade = grade
    self.university = university
  
  def introduce(self):
    print(f"Hello, I'm {self.name} and I'm studying {self.grade} in {self.university} University.")

class Worker(Person):
  def __init__(self, name, surname, age, work):
    super().__init__(name, surname, age)
    self.work = work

  def introduce(self):
    print(f"Hello, I'm {self.name} and I'm work as {self.work}")

student1 = Student("Carlos", "Garcia", 20, "Music", "UBA")
worker1 = Worker("Elon", "Musk", "42", "CEO")

student1.introduce()
worker1.introduce()