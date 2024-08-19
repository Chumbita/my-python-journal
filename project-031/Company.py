class Company:
  def __init__(self):
    self.employees = []
  
  def filter_employees(self, department, min_value):
    list_of_employee = [employee for employee in self.employees if employee.department == department and employee.qualification_average() >= min_value]
    return list_of_employee

  def increase_qualifications(self, department, percentage):
    employees = [employee for employee in self.employees if employee.department == department]
    x = [setattr(employee, 'qualifications', [qualification * (percentage/100 + 1) for qualification in employee.qualifications]) for employee in employees]
    return employees
  