#function to read the given number n from a file
def getNum():
    try:
        #take the file name as input
        file_name = input()
        #open the file to read
        with open(file_name, "r") as file:
            #read the number from the file and convert it to an integer
            number = int(file.read().strip())
        return number
    except FileNotFoundError:
        print("File not found!")
        return None
    except ValueError:
        print("Invalid data format!")
        return None

#function to compute Fibonacci number for a given n
def compute_fibonacci(n):
    #base cases for n=0 and n=1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    #iterative calculation for n>=2
    fib_1, fib_2 = 0, 1
    for _ in range(2, n + 1):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    return fib_2

#function to show the given value n and computed value F(n) on the screen
def show(n, fib_n):
    print(f"Fibonacci({n}) = {fib_n}")

#function to write the result to a text file
def saveFile(n, fib_n, validity):
    with open("result.txt", "w") as file:
        if validity:
            file.write(f"Fibonacci({n}) = {fib_n}")
        else:
            file.write("Invalid input!")

#main logic of the program
def main():
    n = getNum()
    if n is None:  #check if reading n was successful
        return

    #check if the input number is within the valid range
    if n < 0 or n > 20:
        print("Invalid input!")
        saveFile(n, None, False)
    else:
        fib_n = compute_fibonacci(n)
        show(n, fib_n)
        saveFile(n, fib_n, True)

#if the script is run directly, execute the main function
if __name__ == "__main__":
    main()
