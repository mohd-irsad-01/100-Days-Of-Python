class Employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print("Employee name:", self.name)
        print("Salary:", self.salary)

class Developer(Employee):
    def __init__(self, name, salary, programing_language):
        super().__init__(name, salary)
        self.programing_language = programing_language

    def show_skills(self):
        print("Programing Language:", self.programing_language)

dev = Developer("Irsad", 25000, "Python")

dev.show_details()
dev.show_skills()
