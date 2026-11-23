class AgeError(Exception):
    # Custom Exception Class
    pass

def check_age(age):
    if age < 18:
        raise AgeError("You are not eligible to vote")
    else:
        print("You are eligible to vote")

try:
    # Taking user input
    age = int(input("Enter your age: "))
    check_age(age)

except AgeError as e:
    # Catch custom error
    print("Error:", e)

except ValueError:
    # Catch invalid input
    print("Please enter a valid number.")

finally:
    # Always executes
    print("Age verification completed.")
