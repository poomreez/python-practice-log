import os

file_path = "text.txt"

if os.path.exists(file_path):
    print(f"This location '{file_path} is exist")
    if os.path.isfile(file_path):
        print(f"This '{file_path} is file")
    elif os.path.isdir(file_path):
        print(f"This '{file_path} is Directory")

else:
    print("This localtion doesn't exist")