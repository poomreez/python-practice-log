def student_info(*names, **info):
    for name in names:
        print(name, end=" ")  
    print()

    print(f"Student Code: {info.get("code")} Major: {info.get("major")}")
    print(f"Date of Birth: {info.get("date")} Blood Group: {info.get("blood").upper()}")
    print(f"Nationality: {info.get("nationality")}", end=" ")
    
    if "religion" in info:
        print(f"Religion: {info.get("religion")}")
    else:
        print()

student_info(
    "Mr.",
    "Jaxson",
    "Wood",
    code="A1011",
    major="Computer Science",
    date="22/11/2004",
    blood="o",
    nationality="American",
    religion="Christian",
)
