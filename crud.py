employees=[]
def add_employee():
    name=input("enter a employee name:")
    employees.append(name)
    print("employee added sucessfully!")
def view_employees():
    if len(employees)==0:
        print("no employees found")
    else:
     print("employee list:")
    for emp in employees:
        print(emp)
def update_employee():
    view_employees()
    old_name=input("enter employee name to update:")
    if old_name in employees:
        new_name=input("enter new name:")
        index=employees.index(old_name)
        employees[index]=new_name
        print("employee updated!")
    else:
        print("employee not found")
def delete_employee():
    view_employees()
    name=input ("enter employee name to delete:")
    if name in employees:
        employees.remove(name)
        print("employee deleted")
    else:
        print("employee not found")
while True:
    print("\n1.ADD 2.VIEW 3.UPDATE 4.DELETE 5.EXIT")
    choice=input("enter choice:")
    if choice=="1":
        add_employee()
    elif choice=="2":
        view_employees()
    elif choice=="3":
        update_employee()
    elif choice=="4":
        delete_employee()
    elif choice=="5":
        print("exiting program")
        break
    else:
        print("invalid choice")
