import sys

# AssertionError is raised when an assertion or condition is not met.

def main():
    # Check if there is more or less than 1 argument (excluding the script name)
    if len(sys.argv) != 2:
        raise AssertionError("more than one argument is provided")

    # Check if the argument is an integer
    try:
        number = int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")

    # Check if the number is even or odd
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

if __name__ == "__main__":
    main()

