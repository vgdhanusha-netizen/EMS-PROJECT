class Employee :
          def __init__(self, emp_id,emp_name, emp_age,emp_dept,emp_salary):
                self.emp_id=emp_id
                self.emp_name=emp_name         
                self.emp_age=emp_age
                self.emp_dept=emp_dept
                self.emp_salary=emp_salary
          def display(self):
                print("id:",self.emp_id)
                print("name:",self.emp_name)
                print("age:",self.emp_age)
                print("dept:",self.emp_dept)
                print("salary:",self.emp_salary)
          def update_salary(self, new_salary):
                self.emp_salary = new_salary
                print("salary updated")
e1 = Employee(101,"dhanu",20,"it",15000)
e1.display()