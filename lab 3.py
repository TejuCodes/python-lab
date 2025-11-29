# Program: Division with Exception Handling

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Please enter valid numbers.")



try:
    f = open("data.txt", "r")
    print(f.read())

except FileNotFoundError:
    print("File not found!")

finally:
    print("File operation completed.")
