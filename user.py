# Marclin Abarracoso BSIT2-B1
from api import curl_command
import json, webbrowser, os
from datetime import datetime

def Main():
    print ("""
        Employees (Sample DB) CRUD
        URL: http://127.0.0.1:5000/main
        OPERATIONS YOU CAN DO
        [1] Add New Employee Record
        [2] Retrieve Employees
                To display all employee records, add '/employees' to the URL
                To search employee by Employee ID, add '/employees/employee ID number' to the URL
        [3] Update Employee
        [4] Delete Employee Record
        [5] Exit
                Disclaimer: Make sure that the api.py is running in background before exploring this file. :>\n""")
    input1 = int(input('\nChoose Operation: '))


    # add
    if input1 == 1:
        print()
        emp_id = int(input('Input Employee ID: '))
        edate = str(input('Input End Date (YYYY-MM-DD): '))
        first_name = str(input('Input First Name: '))
        last_name = str(input('Input Last Name: '))
        sdate = str(input('Input Start Date (YYYY-MM-DD): '))
        title = str(input('Input Title: '))
        assigned_branch_id = int(input('Input Assigned Branch ID: '))
        dept_id = int(input('Input Department ID: '))
        superior_emp_id = int(input('Input Superior Employee ID: '))

        endate = datetime.strptime(edate, "%Y-%m-%d").date()
        end_date = endate.strftime("%Y-%m-%d")
        stdate = datetime.strptime(sdate, "%Y-%m-%d").date()
        start_date = stdate.strftime("%Y-%m-%d")

        data_list = {
            'emp_id' : emp_id,
            'end_date' : end_date,
            'first_name' : first_name,
            'last_name' : last_name,
            'start_date' : start_date,
            'title' : title,
            'assigned_branch_id' : assigned_branch_id,
            'dept_id' : dept_id,
            'superior_emp_id' : superior_emp_id
        }
        
        url = 'http://127.0.0.1:5000/main/employees'
        json_data = json.dumps(data_list)

        command = ['curl', '-X', 'POST', '-H', 'Content-Type: application/json', '-d', json_data, url]
        curl_command(command)

        forma = int(input("""In what format do you want to display the new added record?
            [1] JSON Format
            [2] XML Format

        Choose (1/2): """))
        if forma == 1:
            print('\nSuccessfully added new record.')
            webbrowser.open(f'http://127.0.0.1:5000/main/employees/{emp_id}')
        elif forma == 2:
            print('\nSuccessfully added new record.')
            webbrowser.open(f'http://127.0.0.1:5000/main/employees/{emp_id}?format=xml')

        again_choice()


    # retrieve
    elif input1 == 2:
        print("""\nOperations:
        [1] Retrieve all employee records
        [2] Search by ID number
        """)
        input2 = int(input("\nChoose Operation: "))
        if input2 == 1: 
            forma = int(input("""\nIn what format do you want to display the chosen operation?
            [1] JSON Format
            [2] XML Format
        
        Choose (1/2): """))
            if forma == 1:
                command = ('curl', 'http://127.0.0.1:5000/main/employees')
                curl_command(command)
                webbrowser.open('http://127.0.0.1:5000/main/employees')
            elif forma == 2:
                command = ('curl', 'http://127.0.0.1:5000/main/employees?format=xml')
                curl_command(command)
                webbrowser.open('http://127.0.0.1:5000/main/employees?format=xml')
            again_choice()
            
        elif input2 == 2:
            emp_id = int(input("Input ID number to search: "))
            if emp_id > 20:
                print('Database only consists of 19 records.')
                os.system('cls')
                Main()
            else:
                forma = int(input("""\nIn what format do you want to display the chosen operation?
                [1] JSON Format
                [2] XML Format
            
            Choose (1/2): """))
                if forma == 1:
                    # search_id(emp_id)
                    command = ('curl', f'http://127.0.0.1:5000/main/employees/{emp_id}')
                    curl_command(command)
                    webbrowser.open(f'http://127.0.0.1:5000/main/employees/{emp_id}')
                elif forma == 2:
                    command = ('curl', f'http://127.0.0.1:5000/main/employees/{emp_id}?format=xml')
                    curl_command(command)
                    webbrowser.open(f'http://127.0.0.1:5000/main/employees/{emp_id}?format=xml')
            
            again_choice()

    # update
    elif input1 == 3:
        print()
        emp_id = int(input("Input ID number to update: "))
        if emp_id > 20:
            print('Database only consists of 19 records.')
            os.system('cls')
            Main()
        else:
            get_rec = ('curl', '-X', 'GET', f'http://127.0.0.1:5000/main/employees/{emp_id}')
            curl_command(get_rec)

            edate = str(input('Input End Date (YYYY-MM-DD): '))
            first_name = str(input('Input First Name: '))
            last_name = str(input('Input Last Name: '))
            sdate = str(input('Input Start Date (YYYY-MM-DD): '))
            title = str(input('Input Title: '))
            assigned_branch_id = int(input('Input Assigned Branch ID: '))
            dept_id = int(input('Input Department ID: '))
            superior_emp_id = int(input('Input Superior Employee ID: '))

            endate = datetime.strptime(edate, "%Y-%m-%d").date()
            end_date = endate.strftime("%Y-%m-%d")
            stdate = datetime.strptime(sdate, "%Y-%m-%d").date()
            start_date = stdate.strftime("%Y-%m-%d")

            data_list = {
            'end_date' : end_date,
            'first_name' : first_name,
            'last_name' : last_name,
            'start_date' : start_date,
            'title' : title,
            'assigned_branch_id' : assigned_branch_id,
            'dept_id' : dept_id,
            'superior_emp_id' : superior_emp_id
            }
        
            url = (f'http://127.0.0.1:5000/main/employees/{emp_id}')
            json_data = json.dumps(data_list)

            forma = int(input("""\nIn what format do you want to display the updated record?
                [1] JSON Format
                [2] XML Format

            Choose (1/2): """))
            if forma == 1:
                command = ('curl', '-X', 'PUT', '-H', 'Content-Type: application/json', '-d', json_data, url)
                curl_command(command)
                print('\nSuccessfully updated a record.')
                webbrowser.open(f'http://127.0.0.1:5000/main/employees/{emp_id}')
            elif forma == 2:
                command = ('curl', '-X', 'PUT', '-H', 'Content-Type: application/json', '-d', json_data, url)
                curl_command(command)
                print('\nSuccessfully updated a record.')
                webbrowser.open(f'http://127.0.0.1:5000/main/employees/{emp_id}?format=xml')

            again_choice()

    # delete
    elif input1 == 4:
        print ()
        print ("Please provide employee ID number to delete.")
        emp_id = int(input("Employee ID: "))
        get_rec = ('curl', '-X', 'GET', f'http://127.0.0.1:5000/main/employees/{emp_id}')
        curl_command(get_rec)
        input3 = str(input("Continue delete? (y/n): "))
        if input3 == 'y':
            del_rec = ('curl', '-X', 'DELETE', f'http://127.0.0.1:5000/main/employees/{emp_id}')
            curl_command(del_rec)
            print('\nSuccessfully deleted record.')
            webbrowser.open('http://127.0.0.1:5000/main/employees')
        else:
            os.system('cls')
            Main()

        again_choice()
        

    elif input1 == 5:
        print("\nThank you!\n")
        exit()

def again_choice():
    choice = str(input("\nDo you want to choose another operation? (y/n): "))
    if choice == 'y':
        os.system('cls')
        Main()
    elif choice == 'n':
        print("\nThank you!\n")
        exit()


Main()