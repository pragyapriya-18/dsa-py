class Student:
    def __init__(self, name, id, department):
        self.name = name
        self.id = id
        self.department = department

    # Set and Get methods for Name
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    # Set and Get methods for ID
    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    # Set and Get methods for Department
    def set_department(self, dept):
        self.department = dept

    def get_department(self):
        return self.department

    # Print all info
    def __str__(self):
        return 'Name:' +  self.name + '\nid:' + self.id + '\nDepartment:' + self.department

import time

# Measure execution time using perf_counter() before calling main()
start_time = time.perf_counter()

def main():
    # Create a Student object
    student_obj = Student("Pragya", "12345", "Computer Science")
    
    # Print student details
    print(student_obj)

# Call the main function
main()

# Measure the end time after main()
end_time = time.perf_counter()

# Print execution time
print("Time=",end_time - start_time)