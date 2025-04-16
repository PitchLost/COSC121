'''
A lecturer wants to send a congratulatory email to all students who obtained a 
grade of A+ in a recent test. 

Write a function email_list(test_results) that takes as a parameter a list of 
(username, grade) tuples and returns a list of email addresses of students 
with an A+ grade. 
'''

def email_list(test_results):
    '''Yep'''
    return_list = []
    for i, result in enumerate(test_results):
        email, test_result = result
        if test_result == 'A+': 
            return_list.append(f"{email}@uclive.ac.nz")
    return return_list
        

test_grades = [
    ('amg001', 'C-'),
    ('pro999', 'A+'),
    ('axi010', 'B+'),
    ('mix123', 'A'),
    ('mix124', 'A-'),
    ('frd005', 'C+'),
    ('mnb900', 'D'),
    ('afw005', 'E'),
    ('rdr099', 'A+')
]
for email in email_list(test_grades):
    print(email)