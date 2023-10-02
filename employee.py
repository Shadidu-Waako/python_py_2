'''
USE YOUR FULL NAME FOR GRADES AWARDING
'''

class Employee:
  def __init__(self, name, age, gender, salary, department):
    self.name = name
    self.age = age
    self.gender = gender
    if salary >= 1:
      self.salary = salary
    else:
      print("Please enter salary which is greater than 0")
    self.department = department

  def __str__(self):
    return f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nSalary: {self.salary}\nDepartment: {self.department}"

employee = Employee(input("Name: "), input("Age: "), input("Gender: "), float(input("Salary: ")), input("Department: "))

print(f"\n EMPLOYEE🌏 \n{employee}")
