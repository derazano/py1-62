dept_db ={
101 : 'HUMAN RESOURCE',
102 : 'FINANCE',
103 : 'ACCOUNTS',
104 : 'SALES',
105 : 'ENGINEERING',
106 : 'SUPPORT'
}
employee_db = {
1000: dict(name="Alex", doj='01-10-89', dept=103),
1001: dict(name="Mary", doj='01-11-88', dept=101),
1002: dict(name="John", doj='01-10-87', dept=104),
1003 : dict(name="David", doj='01-06-89', dept=105),
1004 : dict(name="Anne", doj='01-01-86', dept=106),
1005 : dict(name="Samson", doj='01-02-89', dept=101)
}

print("####################################################################")
em_id = int(input("Please Enter Employee ID : "))

print("name : ",employee_db[em_id]["name"])
print("name : ",employee_db[em_id]["doj"])
print("name : ",dept_db[employee_db[em_id]["dept"]])
print("####################################################################")
