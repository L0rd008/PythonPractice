#define lists of subjects and actions
subjects = ['I', 'We']
actions = ['play', 'watch']

#read input for sports and split it into a list
sports = input().strip().split()

#ensure exactly two sports are provided
if len(sports) != 2:
    print("Please enter exactly two sports.")
else:
    #generate sentences using nested loops
    for subject in subjects:
        for action in actions:
            for sport in sports:
                print(f'{subject} {action} {sport}.')
