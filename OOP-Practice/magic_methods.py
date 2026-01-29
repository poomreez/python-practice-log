class Job:

    def __init__(self, name, position, salary):  # Magic method for build object
        self.name = name
        self.position = position
        self.salary = salary
        self.item = []

    def __str__(self):  # __str__ for print (use this for don't output internal info)
        return (f"Name: {self.name} | Postition: {self.name} | Salary: {self.salary:,} USD")

    def __eq__(self, other):  # __eq__ for equal (self equal compare == with other[self])
        return self.salary == other.salary

    def __len__(self):  # __len__ for check len of object..
        return len(self.salary)

    def __contains__(self, keyword):  # __contain__ for find keyword in object (ctrl+F)
        return (keyword in self.position)  # ex. find "Engineer" position in self.positon
    
    def __getitem__(self, key): # __getitem__ for find value by key (like key/value in dict)
        if key == "name":       # ex. find key "name" of employee1 out will be "Trey"
            return self.name
        elif key == "position":
            return self.position
        elif key == "salary":
            return f"{self.salary:,} USD"
        else:
            return f"{key} was not found"

# Creat objects
employee1 = Job("Trey", "Engineer", 15000)
employee2 = Job("Bob", "Manager", 20000)

# Call
# __str__
print(employee1)  # Output: Name: Trey | Position: Engineer } | Salary: 15,000 USD
# __eq__
print(employee1.salary == employee2.salary)  # Output: False (15000 not equal 20000)
# __con__
print("Engineer" in employee1) # Output: True (employee1 is "Engineer")
# __getitem__
print(employee2["name"]) # Output: Bob (find name(key) of employee2(object)))
