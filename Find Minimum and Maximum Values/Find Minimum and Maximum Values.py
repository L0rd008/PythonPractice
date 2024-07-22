# Read input from the user, split by spaces, and convert each part to a float
try:
    flt_list = [float(num) for num in input().split()]
    if len(flt_list) != 10:
        raise ValueError("You must enter exactly 10 numbers.")
except ValueError as e:
    print(f"Invalid input: {e}")
else:
    # Print the minimum and maximum values from the list
    print(f"Minimum = {min(flt_list)}")
    print(f"Maximum = {max(flt_list)}")
