# Marclin Abarracoso BSIT2-B1
from flask import Flask, make_response, jsonify, request, Response
from flask_mysqldb import MySQL
import subprocess
import xml.etree.ElementTree as ET
import xml.dom.minidom

app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "marclin"
app.config["MYSQL_DB"] = "sampledb"

app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

# for curl
def curl_command(command):
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)

# for xml format
def xml_format(data_list, root_element="root"):
    root = ET.Element(root_element)
    for data in data_list:
        element = ET.SubElement(root, "employee")
        for key, value in data.items():
            sub_element = ET.SubElement(element, key)
            sub_element.text = str(value)
    
    stringxml = ET.tostring(root, encoding='utf-8', method='xml')
    xmlfinal = xml.dom.minidom.parseString(stringxml).toprettyxml(indent="  ")
    return xmlfinal

# data fetch from database
def data_fetch(query):
    cur = mysql.connection.cursor()   
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    data = [{k: v.decode() if isinstance(v, bytes) else v for k, v in item.items()} for item in data]
    return data

# main page
@app.route("/main")
def main_page():
    return Response("""
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
                Disclaimer: Make sure that the api.py is running in background before exploring this file. :>\n""", mimetype="text/plain")


# add record
@app.route("/main/employees", methods=['POST'])
def add_employee():
    info = request.get_json()
    emp_id = info['emp_id']
    end_date = info['end_date']
    first_name = info['first_name']
    last_name = info['last_name']
    start_date = info['start_date']
    title = info['title']
    assigned_branch_id = info['assigned_branch_id']
    dept_id = info['dept_id']
    superior_emp_id = info['superior_emp_id']
    
    query = f"INSERT INTO employee (emp_id, end_date, first_name, last_name, start_date, title, assigned_branch_id, dept_id, superior_emp_id) \
         VALUES ({emp_id}, '{end_date}', '{first_name}', '{last_name}', '{start_date}', '{title}', {assigned_branch_id}, {dept_id}, {superior_emp_id})"
    data_fetch(query)
    mysql.connection.commit()

    return make_response(jsonify('New record has been added.'), 21,)


# # retrieve (display) all employess 
@app.route("/main/employees", methods=['GET'])
def get_employees():
    data = data_fetch("""select * from employee""")
    
    formatformat = request.args.get('format')
    if formatformat == 'xml':
        response = xml_format(data, root_element="Employees")
        return Response(response, content_type='application/xml')
    else:
        return make_response(jsonify(data), 20)
    

# retrieve by employee id
@app.route("/main/employees/<int:emp_id>", methods=['GET'])
def search_id(emp_id):
    data = data_fetch(f""" select * from employee where emp_id = {emp_id}""")

    formatformat = request.args.get('format')
    if formatformat == 'xml':
        response = xml_format(data, root_element="Employees")
        return Response(response, content_type='application/xml')
    else:
        return make_response(jsonify(data), 20)


# update
@app.route("/main/employees/<int:emp_id>", methods=['PUT'])
def update_emprec(emp_id):
    info = request.get_json()
    end_date = info['end_date']
    first_name = info['first_name']
    last_name = info['last_name']
    start_date = info['start_date']
    title = info['title']
    assigned_branch_id = info['assigned_branch_id']
    dept_id = info['dept_id']
    superior_emp_id = info['superior_emp_id']

    query = f"""update employee set 
               end_date = '{end_date}',
               first_name = '{first_name}',
               last_name = '{last_name}',
               start_date = '{start_date}',
               title = '{title}',
               assigned_branch_id = '{assigned_branch_id}',
               dept_id = '{dept_id}',
               superior_emp_id = '{superior_emp_id}'
               where emp_id = '{emp_id}'
               """
    data_fetch(query)
    mysql.connection.commit()

    return make_response(jsonify(f"Employee number {emp_id} records have been successfully updated."), 20)


# delete
@app.route("/main/employees/<int:emp_id>", methods=['DELETE'])
def delete_record(emp_id):
    data_fetch(f""" delete from employee where emp_id = {emp_id} """)
    mysql.connection.commit()
    return make_response(jsonify(f"Employee number {emp_id} records has been successfully deleted"), 20)

if __name__=='__main__':
    app.run(debug=True)