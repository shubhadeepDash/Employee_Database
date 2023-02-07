import add_mod
import employee_module
def login_function():
    print("-------WELCOME TO EMPLOYEE SYSTEM--------\n")
    login_id = input("Please Enter Login ID:")
    password = input("Please Enter Passoword:")
    file = open("login.txt","r")
    x = file.readlines()
    for i in x:
        if login_id + " " + password + "\n" in x:
            if login_id == "admin":
                add_mod.admin_function()
            else:
                employee_module.employee_function(login_id)
        else:
            print("\nInvalid Login ID or Password!!!")
    file.close()