# task2_write_append.py

user_input = input("Enter a value: ")

# Write to file
with open("output.txt", "w") as file:
    file.write(f"User entered: {user_input}\n")

# Append data
with open("output.txt", "a") as file:
    file.write("This is appended data.\n")

# Read and display final content
with open("output.txt", "r") as file:
    print("\nFinal file content:")
    print(file.read())
