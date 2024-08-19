class Employee:
  def __init__(self, name, department, qualifications):
    self.name = name
    self.department = department
    self.qualifications = qualifications

  def qualification_average(self):
    number_qualification = len(self.qualifications)
    average = 0
    for qualification in self.qualifications:
      average += qualification
    average /=number_qualification
    return average