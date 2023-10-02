class Employee:
  def __init__(self, name, age, gender, salary, department):
    self.name = name
    self.age = age
    self.gender = gender
    self.salary = salary
    self.department = department

  def __str__(self):
    return f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nSalary: {self.salary}\nDepartment: {self.depaartment}"

number_of_employees = int(input("Enter number of empolyees: \n"))
for employee in number_of_employees:
  print(f"Enter Employee {employee + 1} details")
  employee{employee + 1} = Employee(input("Name: "), int(input("Age: ")), input("Gender: "), input("Salary: "), input("Department: "))

for employee in number_of_employees:
  print(f"Employee{employee + 1}: {employee}")
