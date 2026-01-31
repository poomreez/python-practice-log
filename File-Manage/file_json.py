import json

file_path = "C:/Users/thebu/OneDrive/Desktop/input.json"

data = {
    "name": "Bob",
    "age": 30,
    "city": "London"
}

# Write
with open(file_path, "w") as file_write:
    json.dump(data, file_write, indent=4)

# Read
with open(file_path, "r") as file_read:
    content = json.load(file_read)

print(content)

# Append
new_data = {"name": "Sadie", "age": 25, "city": "New York"}

# 1. read
with open(file_path, "r") as file:
    data = json.load(file)

# 2. modify
data.append(new_data)

# 3. write back
with open(file_path, "w") as file_append:
    json.dump(data, file_append, indent=4)
