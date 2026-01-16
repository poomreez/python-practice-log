class Employee:
    def get_bonus(self):
        return 1000


class Manager(Employee):
    def get_bonus(self):
        return 5000


staff_1 = Employee()
staff_2 = Manager()

print(staff_1.get_bonus() + staff_2.get_bonus())