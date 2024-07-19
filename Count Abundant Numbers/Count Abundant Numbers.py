def sum_of_proper_divisors(number):
    #initialize the sum with 1 since 1 is a proper divisor of all numbers
    divisor_sum = 1
    #loop through potential divisors from 2 to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            #add both divisors i and number/i to the sum
            divisor_sum += i
            if i != number // i:  # avoid adding the square root twice if it's a perfect square
                divisor_sum += number // i
    return divisor_sum

def count_abundant_numbers(n):
    #count the number of abundant numbers from 2 to n inclusive
    abundant_count = 0
    for number in range(2, n + 1):
        if sum_of_proper_divisors(number) > number:
            abundant_count += 1
    return abundant_count

try:
    upper_limit = int(input('Input number: ')) #take the input number
    if upper_limit < 2:  # avoid invalid inputs
        print('Invalid Input')
    else:
        abundant_count = count_abundant_numbers(upper_limit)
        print(f'Number of abundant numbers from 1 to {upper_limit} is {abundant_count}') #output the number of abundant numbers
except ValueError:
    #handle invalid input (non-integer inputs)
    print("Invalid Input. Please enter a valid integer.")
