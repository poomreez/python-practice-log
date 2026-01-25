# Example : *args(non-key arguments)(Tuple) and **kwargs(keyword arguments)(Dict)
# Title : Student Informations

# Define student_info function with 2 parameters for (*names = *args, **info = **kwargs)
# Use for loop in *names to print full name
def student_info(*names, **info):
    for name in names:
        print(name, end=" ")  # Use kwargs end=" " for one-line output (# Mr. Firstname Lastname)
    print() # print() for space

    # Use if condition for print **info by conditions
    # use kwargs.get("key") to get value in each dict
    if "religion" in info: # If the student put every single informations will print this
        print(f"Student Code: {info.get("code")} Major: {info.get("major")}")
        print(f"Date of Birth: {info.get("date")} Blood Group: {info.get("blood").upper()}")
        print(f"Nationality: {info.get("nationality")} Religion: {info.get("religion")}")
    else:  # If the student don't put religion will print this
        print(f"Student Code: {info.get("code")} Major: {info.get("major")}")
        print(f"Date of Birth: {info.get("date")} Blood Group: {info.get("blood").upper()}")
        print(f"Nationality: {info.get("nationality")}")

# Define *args and *kwargs in student_info function
student_info("Mr.", "Jaxson", "Wood", #*args (*names) before *kwargs (**info)
             code="A1011",
             major="Computer Science",
             date="22/11/2004",
             blood="o",
             nationality="American",
             religion="Christian"
             )
