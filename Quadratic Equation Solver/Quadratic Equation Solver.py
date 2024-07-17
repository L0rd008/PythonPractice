import cmath  # import cmath for complex number operations

def get_coefficient(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

# get inputs with validation
a = get_coefficient('Enter a :')
b = get_coefficient('Enter b :')
c = get_coefficient('Enter c :')

if a == 0:
    print("Coefficient 'a' cannot be zero in a quadratic equation.")
else:
    # calculate the discriminant
    discriminant = b**2 - 4*a*c
    # calculate the two roots
    root_1 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    root_2 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    # print the results
    print(f"Roots are: {root_1.real:.2f} {root_2.real:.2f}" if discriminant >= 0 else f"Roots are: {root_1} {root_2}")
