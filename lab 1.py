# =========================================
#   Combined Program: List, Tuple, Dictionary
# =========================================

print("\n===== LIST OPERATIONS =====")

# List
numbers = [10, 20, 30, 40, 50]
print("Original List:", numbers)

numbers.append(60)
print("After Append:", numbers)

numbers[2] = 35
print("After Updating 3rd element:", numbers)

numbers.remove(40)
print("After Removing 40:", numbers)

print("Slicing (1 to 4):", numbers[1:5])

print("List Elements:")
for n in numbers:
    print(n)


print("\n===== TUPLE OPERATIONS =====")

# Tuple
fruits = ("apple", "banana", "cherry", "banana")
print("Tuple:", fruits)

print("Element at index 1:", fruits[1])
print("Slicing (1 to 3):", fruits[1:3])
print("Count of 'banana':", fruits.count("banana"))
print("Index of 'cherry':", fruits.index("cherry"))


print("\n===== DICTIONARY OPERATIONS =====")

# Dictionary
student = {
    "name": "Teju",
    "age": 20,
    "course": "Python"
}
print("Original Dictionary:", student)

print("Name:", student["name"])

student["mark"] = 92
print("After Adding mark:", student)

student["age"] = 21
print("After Updating Age:", student)

del student["course"]
print("After Deleting Course:", student)

print("Dictionary Items:")
for key, value in student.items():
    print(key, ":", value)

print("\n===== END OF PROGRAM =====")
