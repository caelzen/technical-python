# Goal: Practice adding, updating, and safely retrieving values.

"""
Task: Write a function update_records(records, student_id, new_score) that takes a dictionary
of student IDs and scores. It updates the score for the given ID, or adds the ID if it doesn't
exist. Then, use .get() to safely retrieve the score of a student who might not be in the
dictionary, providing a default value of "Not Found".
"""


initial_records = {
    9001: 85,    # Student ID 9001 has a score of 85
    9002: 92,    # Student ID 9002 has a score of 92
    9003: 78,    # Student ID 9003 has a score of 78
    9004: 95     # Student ID 9004 has a score of 95
}

def update_records(records, student_id, new_score):
	records[student_id] = new_score
		

update_records(initial_records, 9001, 76)
update_records(initial_records, 9000, 89)
missing_score = initial_records.get(9005, 'Not Found')

# --- Final State and Output ---
print('Final Records: {}'.format(initial_records))
print('Retrieved Score (9005): {}'.format(missing_score))