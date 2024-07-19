def is_prime(number):
    #check if the number is less than 2
    if number < 2:
        return False
    #check if the number is 2, which is the only even prime number
    if number == 2:
        return True
    #eliminate even numbers greater than 2
    if number % 2 == 0:
        return False
    #check divisibility by odd numbers from 3 to the square root of the number
    sqrt_number = int(number ** 0.5)
    for divisor in range(3, sqrt_number + 1, 2):
        if number % divisor == 0:
            return False
    return True

while True:
    try:
        number = int(input()) #taking input number
        if number < 0: #stopping the program after negative input
            break
        #print 'prime' or 'non-prime' based on the result
        if is_prime(number):
            print('prime')
        else:
            print('non-prime')
    except ValueError:
        print("Invalid input. Please enter an integer.")
