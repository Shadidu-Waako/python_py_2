class Employee:
  def __init__(self, name, age, gender, salary, department):
    self.name = name
    self.age = age
    self.gender = gender
    self.salary = salary
    self.department = department

  def __str__(self):
    return f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nSalary: {self.salary}\nDepartment: {self.department}"

employee = Employee(input("Name: "), input("Age: "), input("Gender: "), input("Salary: "), input("Department: "))

print(f"Employee: {employee}")
