case_number = 1  # Initialize the case number

while True:
    x = int(input())  # Read the integer x

    if x == 0:
        break  # Exit the loop if x is 0

    # Print the formatted output
    print(f"Case {case_number}: {x}")

    case_number += 1  # Increment the case number