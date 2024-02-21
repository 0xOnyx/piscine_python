from new_student import Student

student = Student(name="Edward", surname="agle")
print(student)

try:
    Student = Student(name="Edward", surname="agle", id="toto")
except TypeError as e:
    print(f"TypeError: {e}")
