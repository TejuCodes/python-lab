# List example
numbers = [10, 20, 30, 40]

# Methods
numbers.append(50)         # Add at end
numbers.insert(1, 15)      # Insert at position
numbers.remove(30)         # Remove value
numbers.pop()              # Remove last item
numbers.sort()             # Sort list
numbers.reverse()          # Reverse list

# Built-in functions
print("Length:", len(numbers))      # Count items
print("Maximum:", max(numbers))     # Largest value
print("Minimum:", min(numbers))     # Smallest value
print("Sum:", sum(numbers))         # Sum of values

print("Final List:", numbers)


# Tuple example
colors = ("red", "green", "blue", "green")

# Methods
print("Count of 'green':", colors.count("green"))
print("Index of 'blue':", colors.index("blue"))

# Built-in functions
print("Length:", len(colors))
print("Maximum:", max(colors))     # Alphabetically greatest
print("Minimum:", min(colors))     # Alphabetically smallest



# Dictionary example
student = {
    "name": "Teju",
    "age": 22,
    "course": "MSc CS"
}

# Methods
print(student.keys())        # List of keys
print(student.values())      # List of values
print(student.items())       # List of key-value pairs

student.update({"age": 23})  # Update value
student.pop("course")        # Remove a key-value pair

# Built-in function
print("Length:", len(student))

print("Final Dictionary:", student)
