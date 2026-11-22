try:
    # Taking user input
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Division operation (may cause error)
    result = num1 / num2 

    print("Result:", result)

except ZeroDivisionError:
    # Handles division by zero error
    print("Error: Cannot divide by zero")

except ValueError:
    # Handles invalid input like letters
    print("Error: Please enter valid numbers")

else:
    # Executes if no error occurs
    print("Calculation completed successfully")

finally:
    # Always executes
    print("Program execution finished.")
