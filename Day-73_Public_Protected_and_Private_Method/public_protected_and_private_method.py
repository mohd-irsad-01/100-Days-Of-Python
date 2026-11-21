class Student:

    def __init__(self):
        self.name = "Irsad"          # Public Member
        self._age = "22"             # Protected Member
        self.__salary = 25000        # Private Member

    def show_details(self):
        print("Name", self.name)
        print("Age", self._age)
        print("Salary", self.__salary)

student = Student()

# Accessing Public Member
print("Public Member:", student.name)

# Accessing Protected Member
print("Protected Member:", student._age)

# Accessing Private Member
print("Private Member:", end=" ")
student.show_details()
