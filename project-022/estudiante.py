class Student:
  def __init__(self, name, age, grade):
    self.name = name
    self.age = age
    self.grade = grade
  
  def estudiar(self):
    print(f"El estudiante {self.name} esta estudiando.")

student_name = input("Student name: ")
student_age = int(input("Student age: "))
student_grade = input("Studen grade: ")

student1 = Student(student_name, student_age, student_grade)

print(f'Name: {student1.name}, age: {student_age}, grade: {student_grade}')
student1.estudiar()