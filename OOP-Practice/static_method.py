class Job:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    @staticmethod  # Add @staticmethod
    def active_position(position):  # No need object data(attributes) X
        active = ["Data Engineer", "Data Analyst", "Product Manager"]
        return True if position in active else False


# Call
print(Job.active_position("Product Manager"))
# class.method()
