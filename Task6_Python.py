def iterateDictionary(key, students):
        print([s[key] for s in students])

students=  [{'student_name': 'jack','student_name': 'micheal','student_name': 'josh','student_name': 'charlie','student_name': 'mohamed','student_name': 'aden','student_name': 'wendy','student_name': 'olivia','student_name': 'ollie','student_name': 'lewis'}]
print("student names...")
iterateDictionary('student_name', students)