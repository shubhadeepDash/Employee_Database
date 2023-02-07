def employee_function(emp_id):
    if "EP" in emp_id:
        print("\n-----------WELCOME TO THE TO EMPLOYEE MODULE---------------\n")
        file = open("add_employee.txt","r")
        j = file.readlines()
        w_list = []
        for i in j:
            if emp_id in i:
                w_list.append(i)
                n = w_list[0].split()[1]
                name = n.strip("Employee_Name:")
        file.close()
        print(f"Welcome, {name}!!!")
        choice = 0
        while(choice != 3):
            print("ENTER 1 - TO VIEW OWN DETAILS")
            print("ENTER 2 - TO VIEW ALL HR NAMES")
            print("ENTER 3 - TO EXIT")
            choice = int(input())
            if choice == 1:
                file = open("add_employee.txt","r")
                j = file.readlines()
                for i in j:
                    if emp_id in i:
                        print(i.replace("\t\t","\n")) 
                    
            elif choice == 2:
                file = open("add_hr.txt","r")
                k = file.readlines()
                el = []
                for i in k:
                    if i not in el:
                        print(i.replace("\t\t","\n")) 

            elif choice == 3:
                break
         
    
    elif "HR" in emp_id:
        print("\n-----------WELCOME TO THE TO EMPLOYEE MODULE---------------\n")
        file = open("add_employee.txt","r")
        j = file.readlines()
        w_list = []
        for i in j:
            if emp_id in i:
                w_list.append(i)
                n = w_list[0].split()[1]
                name = n.strip("Employee_Name:")
        file.close()
        print(f"Welcome, {name} from HR!!!")
        choice = 0
        while(choice != 3):
            print("ENTER 1 - TO VIEW OWN DETAILS")
            print("ENTER 2 - TO VIEW EMPLOYEES")
            print("ENTER 3 - TO EXIT")
            choice = int(input())
            if choice == 1:
                file = open("add_employee.txt","r")
                j = file.readlines()
                for i in j:
                    if emp_id in i:
                        print(i.replace("\t\t","\n"))
                file.close()
            
            elif choice == 2:
                desig = input("Enter designation: ")
                if desig == "ALL" :
                    file = open("add_employee.txt","r")
                    k = file.readlines()
                    le = []
                    for i in k:
                        if i not in le:
                            print(i.replace("\t\t","\n")) 
                    file.close()
                file = open("add_employee.txt","r")
                j = file.readlines()
                for i in j:
                    if desig in i:
                        print(i.replace("\t\t","\n")) 