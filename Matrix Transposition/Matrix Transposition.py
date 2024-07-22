def main():
    matrix = []  # List to store the matrix rows
    try:
        row_length = None  # Variable to store the length of the first row

        while True:
            row_input = input()
            if row_input == '-1':  # Stop input when '-1' is entered
                break

            row = row_input.split()  # Split the input row into elements

            # Check if the current row length matches the previous rows' length
            if row_length is None:
                row_length = len(row)  # Set the row length for the first row
            elif len(row) != row_length:
                raise ValueError("Invalid Matrix")  # Raise an error for inconsistent row lengths

            # Convert each element in the row to an integer
            matrix.append([int(element) for element in row])

        # Transpose the matrix using zip
        transposed_matrix = zip(*matrix)

        # Print the transposed matrix
        for transposed_row in transposed_matrix:
            print(' '.join(map(str, transposed_row)))

    except ValueError as ve:
        print(ve)  # Print the error message for invalid matrix
    except Exception:
        print("Error")  # Handle any other exceptions

if __name__ == "__main__":
    main()
