#Goal: Practice accessing and manipulating data in a nested dictionary structure.

"""
Task: Given a dictionary where keys are department names and values 
are dictionaries of employees (key: name, value: status), write 
a function count_active_employees(company_data) that counts the 
total number of employees across all departments whose status is 'Active'.
"""

department_roster = {
    'Sales': {
        'Alice Johnson': 'Active',
        'Bob Smith': 'Inactive',
        'Carol Vega': 'Active',
        'David Liu': 'Active',
        'Eve Martin': 'Inactive'
    },
    'Engineering': {
        'Frank Lee': 'Active',
        'Grace Hall': 'Active',
        'Henry Kim': 'Inactive',
        'Ivy Ray': 'Active'
    },
    'Marketing': {
        'Jack Green': 'Active',
        'Kate White': 'Active'
    },
    'Finance': {
        'Liam Brown': 'Inactive',
        'Mia Lopez': 'Active',
        'Noah Cruz': 'Active',
        'Owen Price': 'Active'
    }
}


def count_active_employees(company_data):
	counter = 0
	for department, employees in company_data.items():
		for employee, status in employees.items():
			if status == 'Active':
				counter += 1
	return counter

print(count_active_employees(department_roster))