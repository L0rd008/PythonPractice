def calculate_day_of_week(y, m, d):
    #if the month is less than 3, adjust the month and year
    if m < 3:
        m += 12
        y -= 1
    
    #calculate intermediate values a and b
    a = (2 * m) + (6 * (m + 1) // 10)
    b = y + (y // 4) - (y // 100) + (y // 400)
    
    #calculate the day of the week
    f1 = d + a + b + 1
    f = f1 % 7
    
    return f

#read input, split it into year, month, and day, and convert them to integers
input_list = input().split()
y, m, d = int(input_list[0]), int(input_list[1]), int(input_list[2])

#calculate the day of the week
day_of_week = calculate_day_of_week(y, m, d)

#print the result
print(day_of_week)
