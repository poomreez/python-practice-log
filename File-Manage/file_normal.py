file_path = "C:/Users/thebu/OneDrive/Desktop/input.txt"

data = "Hello World!"

# Write
with open(file_path, "w") as file_write:
    file_write.write(data)

# Read
with open(file_path, "r") as file_read:
    content = file_read.read()
    print(content)
    
# Append
with open(file_path, "a") as file_append:
    file_append.write("\nThis is line 2")
