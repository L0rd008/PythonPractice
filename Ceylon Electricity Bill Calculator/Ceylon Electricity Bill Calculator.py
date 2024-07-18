def calculate_ebill(consumption):
    #constants for tariffs and fixed charges
    FIXED_CHARGE_0_30 = 400
    FIXED_CHARGE_31_60 = 550
    FIXED_CHARGE_61_90 = 650
    FIXED_CHARGE_91_120 = 1500
    FIXED_CHARGE_121_180 = 1500
    FIXED_CHARGE_ABOVE_180 = 2000
    
    UNIT_CHARGE_0_30 = 30
    UNIT_CHARGE_31_60 = 37
    UNIT_CHARGE_0_60_ABOVE = 42
    UNIT_CHARGE_61_90 = 42
    UNIT_CHARGE_91_120 = 50
    UNIT_CHARGE_121_180 = 50
    UNIT_CHARGE_ABOVE_180 = 75

    #calculate the bill based on the consumption
    if consumption <= 60:
        if consumption <= 30:
            #calculate for 0-30 kWh
            bill = consumption * UNIT_CHARGE_0_30 + FIXED_CHARGE_0_30
        else:
            #calculate for 31-60 kWh
            bill = 30 * UNIT_CHARGE_0_30 + (consumption - 30) * UNIT_CHARGE_31_60 + FIXED_CHARGE_31_60
    else:
        if consumption <= 90:
            #calculate for 61-90 kWh
            bill = 60 * UNIT_CHARGE_0_60_ABOVE + (consumption - 60) * UNIT_CHARGE_61_90 + FIXED_CHARGE_61_90
        elif consumption <= 120:
            #calculate for 91-120 kWh
            bill = 60 * UNIT_CHARGE_0_60_ABOVE + 30 * UNIT_CHARGE_61_90 + (consumption - 90) * UNIT_CHARGE_91_120 + FIXED_CHARGE_91_120
        elif consumption <= 180:
            #calculate for 121-180 kWh
            bill = 60 * UNIT_CHARGE_0_60_ABOVE + 30 * UNIT_CHARGE_61_90 + 30 * UNIT_CHARGE_91_120 + (consumption - 120) * UNIT_CHARGE_121_180 + FIXED_CHARGE_121_180
        else:
            #calculate for >180 kWh
            bill = 60 * UNIT_CHARGE_0_60_ABOVE + 30 * UNIT_CHARGE_61_90 + 30 * UNIT_CHARGE_91_120 + 60 * UNIT_CHARGE_121_180 + (consumption - 180) * UNIT_CHARGE_ABOVE_180 + FIXED_CHARGE_ABOVE_180

    return bill

try:
    #get input from the user
    c = int(input("Enter the monthly consumption in kWh: "))
    #check if the consumption is negative
    if c < 0:
        print("Consumption cannot be negative.")
    else:
        #calculate the bill and print it
        bill = calculate_ebill(c)
        print(bill)
except ValueError:
    #handle invalid input
    print("Invalid input. Please enter a valid integer for consumption.")
