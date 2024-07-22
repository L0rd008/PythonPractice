def calculate_student_marks():
    num_students = 4  # Number of students
    num_subjects = 3  # Number of subjects for each student

    marks = []  # Create an empty list to store the marks of each student

    for _ in range(num_students):  # Iterate over each student
        # Read the input and convert each element to an integer
        student_marks = list(map(int, input().split()))
        marks.append(student_marks)  # Add the marks to the list

    for student_marks in marks:
        total_marks = sum(student_marks)  # Calculate the total marks
        average_mark = round(total_marks / num_subjects, 1)  # Calculate the average mark
        print(f'Total: {total_marks} Average: {average_mark}')  # Print the result

calculate_student_marks()
