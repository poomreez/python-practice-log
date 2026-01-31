import csv

file_path = "C:/Users/thebu/OneDrive/Desktop/input.csv"

data = [["name", "age", "city"], # Header
        ["Bob", 30, "London"],
        ["Sadie", 25, "New York"]
        ]

new_row = [["Jax", 28, "Queens"]] 

# Write
with open(file_path, "w", newline="") as file_write:
    writer = csv.writer(file_write)
    writer.writerows(data)

# Read
with open(file_path, "r") as file_read:
    reader = csv.reader(file_read)

    for row in reader:
        print(row["name"], row["age"])

# Append
with open(file_path, "a", newline="") as file_write:
    writer = csv.writer(file_write)
    writer.writerows(new_row)
