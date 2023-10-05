import StudentClass as sc

studentid = 1001
name = 'John'
dob = '10/15/2001'
classification = 'junior'

student1 = sc.Student(studentid,name,dob,classification)

student1.calculate_age()

student1.registration_dates()

print(f"Student Age: {student1.return_age} years")
print(f"Registration Dates: {student1.return_registration()}")