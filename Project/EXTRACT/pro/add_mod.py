def admin_function():
    def add_employee(emp_id, emp_name, emp_DOJ, emp_desig, emp_sal):
        file = open("add_employee.txt","a")
        L=["Employee_ID:",emp_id,"\t\tEmployee_Name:",emp_name,"\t\tEmployee_DOJ:",emp_DOJ,"\t\tEmployee_Designation:",emp_desig,"\t\tEmployee_Salary:",emp_sal,"\n"]
        file.writelines(L)
        file.close()
        f = open("login.txt","a")
        q = emp_name.split()[0]
        LL = [emp_id," ",q,"\n"]
        f.writelines(LL)
        f.close()
       
    def remove_emp(emp_id):
        fle = open("login.txt","r+")
        f = fle.readlines()
        list1 = []
        flag = 0 
        for l in f:
            if emp_id not in l:
                list1.append(l)
            else:
                flag = 1
        if flag == 0:
            print("No such employee found.")
        fle.close()
        fle = open("login.txt","w")
        fle.writelines(list1)
        fle.close()
        
        fle2 = open("add_employee.txt","r")
        s = fle2.readlines()
        flagg = 0
        list2 = []
        for l in s:
            if emp_id not in l:
                list2.append(l)
            else:
                flagg = 1
        if flagg == 0:
            print("No such employee found.")
        fle2.close()
        fle2 = open("add_employee.txt","w")
        fle2.writelines(list2)
        fle2.close()
        
    def add_hr(emp_id):
        file = open("add_employee.txt","r")
        w = file.readlines()
        flag = 0 
        for i in w:
            if emp_id in i:
                flag = 1
                f = open("add_hr.txt","a")
                hr_dept = input("Enter the department of the HR:")
                hr_role = input("Enter the role of the HR:")
                L = ["Employee_ID:",emp_id, "\t\tEmployee_Department:",hr_dept,"\t\tEmployee_Role:",hr_role,"\n"]
                f.writelines(L)
        if flag == 0:
            print("No such employee found.\n")
        file.close()
       
    def remove_hr(emp_id):
        fle2 = open("add_hr.txt","r")
        s = fle2.readlines()
        flagg = 0
        list2 = []
        for l in s:
            if emp_id not in l:
                list2.append(l)
            else:
                flagg = 1
        if flagg == 0:
            print("No such employee found.")
        fle2.close()
        fle2 = open("add_hr.txt","w")
        fle2.writelines(list2)
        fle2.close()
       
    print("\n--------WELCOME TO ADMIN---------\n")
    choice = 0
    while(choice != 5):
        print("\n")
        print("ENTER 1 - TO ADD AN EMPLOYEE")
        print("ENTER 2 - TO REMOVE AN EMPLOYEE")
        print("ENTER 3 - TO ADD HR MEMBER")
        print("ENTER 4 - TO REMOVE HR MEMBER")
        print("ENTER 5 - TO EXIT THE ADMIN")
        choice = int(input())
        if choice == 1:
            emp_id = input("Enter the ID of employee:")
            emp_name = input("Enter the name of the employee:")
            emp_DOJ = input("Enter the Date of Joining of the employee:")
            emp_desig = input("Enter the designation of the employee:")
            emp_sal = "0" # salary was to be taken zero by default
            add_employee(emp_id, emp_name, emp_DOJ, emp_desig, emp_sal)
          
        elif choice == 2:
            emp_id = input("Enter the employee ID to remove: ")
            remove_emp(emp_id)
           
        elif choice == 3:
            emp_id = input("Enter the employee ID:")
            add_hr(emp_id)
           
        elif choice == 4:
            emp_id = input("Enter the employee ID to remove: ")
            remove_hr(emp_id)
            
        else:
            break