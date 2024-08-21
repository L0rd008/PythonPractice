from typing import List, Optional

#read_matrix function reads and validates a matrix input from the user
def read_matrix(n: int, m: int, matrix_name: str) -> Optional[List[List[int]]]:
    try:
        print(f"Enter {matrix_name}:")
        matrix = []
        for i in range(n):
            row = input().split() #read a row and split it into elements
            if len(row) != m: #check if the row has the correct number of columns
                print("Invalid Matrix")
                return None
            matrix.append([int(x) for x in row]) #convert elements to integers and add to the matrix
        return matrix
    except ValueError: #handle cases where conversion to integer fails
        print("Invalid Matrix")
        return None
    except Exception: #catch any other unexpected errors
        print("Error")
        return None

#transpose function computes the transpose of a matrix
def transpose(matrix: List[List[int]]) -> List[List[int]]:
    try:
        return [list(row) for row in zip(*matrix)] #use zip to transpose rows and columns
    except Exception: #catch any unexpected errors
        print("Error")
        return None

#matrix_product function computes the product of matrix A and matrix Bᵀ
def matrix_product(A: List[List[int]], B: List[List[int]]) -> Optional[List[List[int]]]:
    try:
        n = len(A) #number of rows in matrix A
        m = len(A[0]) #number of columns in matrix A
        #compute the product of A and Bᵀ
        result = [[sum(A[i][k] * B[j][k] for k in range(m)) for j in range(n)] for i in range(n)]
        return result
    except Exception: #catch any unexpected errors
        print("Error")
        return None

#display_matrix function prints the matrix in a formatted manner
def display_matrix(matrix: List[List[int]]) -> None:
    try:
        for row in matrix: #iterate through each row
            print(" ".join(map(str, row))) #convert elements to strings and print
    except Exception: #catch any unexpected errors
        print("Error")

#main function to orchestrate the reading, processing, and displaying of matrices
def main():
    try:
        n, m = map(int, input("Enter the dimension: ").split(",")) #read and parse matrix dimensions
        A = read_matrix(n, m, "Matrix A") #read matrix A
        B = read_matrix(n, m, "Matrix B") #read matrix B
        if A is None or B is None: #check if matrices were read successfully
            return
        B_T = transpose(B) #compute the transpose of matrix B
        if B_T is None: #check if transpose was successful
            return
        product_matrix = matrix_product(A, B_T) #compute the product of A and Bᵀ
        if product_matrix is None: #check if product computation was successful
            return
        display_matrix(product_matrix) #display the result
    except Exception: #catch any unexpected errors in the main function
        print("Error")

#if the script is run directly, execute the main function
if __name__ == "__main__":
    main()
