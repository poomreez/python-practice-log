class Employee:
    def __init__(self, name, department, position, salary, active):
        self.name = name
        self.department = department
        self.position = position
        self.salary = salary
        self.active = active

    def show_card(self):
        print("---------- EMPLOYEE CARD ----------")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Positon: {self.position}")
        print("-----------------------------------")

    def get_bonus(self):
        return 1000

    def total_salary(self):
        total = self.salary + self.get_bonus()
        print(f"Total salary : ${total:,}")

class C_Level(Employee):
    def get_bonus(self):
        return 8000

class Manager(Employee):
    def get_bonus(self):
        return 5000

class Engineer(Employee):
    def __init__(self, name, department, position, salary, active, progression):
        super().__init__(name, department, position, salary, active)
        self.progression = progression

    def show_card(self):
        print("---------- EMPLOYEE CARD ----------")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Positon: {self.progression} {self.position}")
        print("-----------------------------------")

    def get_bonus(self):
        return 3000

staff_1 = C_Level("Josh Cornwell", "Financial", "CFO", 400000, True)
staff_2 = Manager("Penelope Thorne", "Marketing", "Project Manager", 250000, True)
staff_3 = Engineer("Mac Morales", "Technology", "Software Engineer", 200000, True, "Senior")
staff_4 = Employee("Jennifer Moore", "Technology", "Data Analyst", 120000, True)
staff_5 = Engineer("Steve McConney", "Technology", "Data Engineer", 220000, True, "Mid-Level")

all_employees = [staff_1, staff_2, staff_3, staff_4, staff_5]

print("\n------- 💰 PAYROLL REPORT 💰 -------")
print(" ")

for emp in all_employees:
    emp.show_card()
    emp.total_salary()
    print(" ")