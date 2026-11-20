class Student:

    def __init__(self, name, age):
        self.name = name
        self.__age = age    # Private variable

    # Getter Method
    def get_age(self):
        return self.__age

    # Setter Method
    def set_age(self, new_age):
        if new_age > 0:
            self.__age = new_age
            print("Age updated successfully")
        else:
            print("Invalid age")

student = Student("Irsad", 22)
print("Student Name:", student.name)
print("Old Age:", student.get_age())

student.set_age(23)

print("Updated Age:", student.get_age())
