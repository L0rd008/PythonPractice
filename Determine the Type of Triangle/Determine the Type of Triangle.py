def get_angle(prompt):
    #this function repeatedly prompts the user for an angle until a valid positive integer is entered
    while True:
        try:
            #try to convert input to an integer
            angle = int(input(prompt))
            #check if the angle is positive
            if angle > 0:
                return angle
            else:
                print("Angle must be a positive integer.")
        except ValueError:
            #handle the case where input is not a valid integer
            print("Invalid input. Please enter a valid integer.")

def determine_triangle_type(angle1, angle2, angle3):
    #check if the angles form a triangle
    if angle1 + angle2 + angle3 == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0:
        #check if all angles are less than 90
        if angle1 < 90 and angle2 < 90 and angle3 < 90:
            return "Acute angled"
        #check if any angle is 90
        elif angle1 == 90 or angle2 == 90 or angle3 == 90:
            return "Right angled"
        #if not acute or right, it must be obtuse
        else:
            return "Obtuse angled"
    else:
        #if the angles do not form a triangle
        return "Angles do not form a triangle"

def main():
    #get the three angles from the user
    angle1 = get_angle("Enter angle 1: ")
    angle2 = get_angle("Enter angle 2: ")
    angle3 = get_angle("Enter angle 3: ")

    #determine the type of the triangle
    result = determine_triangle_type(angle1, angle2, angle3)
    #print the result
    print(result)

if __name__ == "__main__":
    #run the main function if the script is executed
    main()
