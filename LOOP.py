employees=[]
while True:
    print("/n Menu")
    print("1.Add employee")
    print("2.View Employees")
    print("3.Exit")
    choice=input("Enter choice:")
    if choice=="1":
        emp_id=input("Enter id:")
        emp_name=input("Enter name:")
        emp_age=input("Enter age:")
        employees.append({"id": emp_id,"name":emp_name,"age":emp_age})
        print("Employee Added")
    elif choice=="2":
        if len(employees)==0:
            print("no employees")
        else:
            print("\n Employee list:")
            for emp in employees:
                print("ID:",emp["id"],emp["Name:"],"|Name",emp["age:"],"|age")
    elif choice=="3":
        print("Bye")
        break
    else:
        print("invalid choice")

