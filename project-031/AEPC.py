from Company import Company
from Employee import Employee
import os

my_company = Company()
my_company.employees = [
    Employee("Rodolfo Acustico", "Engineering", [8, 7, 9]),
    Employee("Mariana Paredes", "Marketing", [4, 5, 6]),
    Employee("Carlos Soto", "Finance", [2, 3, 4]),
    Employee("Andrea Ríos", "Human Resources", [9, 9, 10]),
    Employee("Fernando García", "Engineering", [6, 5, 7]),
    Employee("Isabel Castillo", "Marketing", [10, 9, 9]),
    Employee("Lucas Pereira", "Finance", [5, 6, 5]),
    Employee("Sofía Núñez", "Human Resources", [3, 4, 3]),
    Employee("Javier López", "Engineering", [7, 8, 7]),
    Employee("Gabriela Torres", "Marketing", [9, 7, 8]),
    Employee("David Martínez", "Finance", [10, 10, 9]),
    Employee("Claudia Ramírez", "Human Resources", [5, 4, 6]),
    Employee("Miguel Hernández", "Engineering", [2, 3, 2]),
    Employee("Lucía Méndez", "Marketing", [8, 8, 9]),
    Employee("Ricardo Sánchez", "Finance", [4, 3, 5]),
    Employee("Laura Flores", "Human Resources", [9, 10, 9]),
    Employee("Pablo Gómez", "Engineering", [6, 5, 4]),
    Employee("Ana Morales", "Marketing", [10, 9, 10]),
    Employee("Santiago Cruz", "Finance", [7, 6, 7]),
    Employee("Natalia Rojas", "Human Resources", [8, 7, 9]),
]

flag = True
while flag:
  os.system('cls')
  print('-----|Analysis of Employee Performance in a Company|-----\n\nMENU:\n1)Filter Employees.\n2)Increase Qualifications.\n3)Exit.\n')
  user_opc = int(input("Choose an operation: "))
  if user_opc == 1: 
    os.system('cls')
    print('-----|Filter Employees|-----\n')
    department = input('Enter the department: ').capitalize()
    min_average = float(input('Enter the min average: '))
    employees = my_company.filter_employees(department, min_average)
    os.system('cls')
    print(f'-----|Filter Employees|-----\nFilter Applied:\n-Department: {department}.\n-Min Average: {min_average}.\n')
    for employee in employees:
      average = employee.qualification_average()
      print(f"NAME: {employee.name} DEPARTMENT: {employee.department} QUALIFICATION AVERAGE: {average:.2f}")
  elif user_opc == 2:
    os.system('cls')
    print('-----|Increase Qualifications|-----\n')
    department = input('Enter the department: ').capitalize()
    increase = float(input('Enter the percentage increase: '))
    employees = my_company.increase_qualifications(department, increase)
    os.system('cls')
    print(f'-----|Increase Qualifications|-----')
    for employee in employees:
      average = employee.qualification_average()
      print(f"NAME: {employee.name} DEPARTMENT: {employee.department} QUALIFICATION AVERAGE: {average:.2f}")
  elif user_opc == 3: 
    flag = False
  else: 
    print("Invalid Option.")
  input('\nPress ENTER to continue...')