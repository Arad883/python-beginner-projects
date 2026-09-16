"""
Advanced Calculator
-------------------
A menu-driven calculator that supports basic arithmetic, scientific
functions, complex numbers, memory storage, and calculation history.
"""

import time
import math

# ---------------------------------------------------------------------------
# GLOBAL STATE
# ---------------------------------------------------------------------------

# Stores the most recent calculations; newest entries are inserted first.
history = []

# Holds a single numeric value that persists between operations.
memory = 0.0

# Maximum number of history entries kept in memory.
HISTORY_LIMIT = 10


# ---------------------------------------------------------------------------
# HELPER FUNCTIONS
# ---------------------------------------------------------------------------

def log_history(expression: str, result) -> None:
    """
    Insert a new entry at the start of the history list and trim the list
    so it never exceeds HISTORY_LIMIT items.
    """
    history.insert(0, f"{expression} = {result}")
    if len(history) > HISTORY_LIMIT:
        history.pop()


def read_numbers(prompt: str = "Enter all numbers separated by space: "):
    """
    Read a line of space-separated numbers and convert each token to float.
    Returns a list of floats.
    """
    raw = input(prompt).split()
    return [float(x) for x in raw]


def read_single_number(prompt: str = "Enter a number: "):
    """Read one numeric value from the user and return it as a float."""
    return float(input(prompt))


# ---------------------------------------------------------------------------
# BASIC ARITHMETIC
# ---------------------------------------------------------------------------

def addition():
    """Sum all numbers entered by the user."""
    nums = read_numbers()
    return sum(nums)


def subtraction():
    """Subtract the second number from the first."""
    n1 = read_single_number("Enter first number: ")
    n2 = read_single_number("Enter second number: ")
    return n1 - n2


def multiplication():
    """Multiply all numbers entered by the user."""
    nums = read_numbers()
    result = 1.0
    for num in nums:
        result *= num
    return result


def division():
    """
    Divide the first number by the second.
    Returns an error string if the divisor is zero.
    """
    n1 = read_single_number("Enter first number: ")
    n2 = read_single_number("Enter second number: ")
    if n2 == 0:
        return "Error: Division by zero"
    return n1 / n2


def average():
    """Return the arithmetic mean of the entered numbers."""
    nums = read_numbers()
    if not nums:
        return "Error: No numbers provided"
    return sum(nums) / len(nums)


def modulus():
    """Return the remainder of dividing the first number by the second."""
    n1 = read_single_number("Enter dividend: ")
    n2 = read_single_number("Enter divisor: ")
    if n2 == 0:
        return "Error: Modulus by zero"
    return n1 % n2


def power():
    """Raise the base to the given exponent."""
    base = read_single_number("Enter base: ")
    exp = read_single_number("Enter exponent: ")
    return base ** exp


def square_root():
    """Return the square root of a non-negative number."""
    n = read_single_number("Enter number: ")
    if n < 0:
        return "Error: Cannot take square root of a negative number"
    return math.sqrt(n)


def percentage():
    """
    Compute the value of a percentage applied to a total.
    Formula: (part / 100) * whole
    """
    part = read_single_number("Enter the percentage value (e.g. 25): ")
    whole = read_single_number("Enter the total value (e.g. 200): ")
    return (part / 100) * whole


# ---------------------------------------------------------------------------
# SCIENTIFIC FUNCTIONS
# ---------------------------------------------------------------------------

def scientific():
    """
    Perform a scientific operation selected by the user.
    Trigonometric inputs are given in degrees and converted to radians.
    """
    print("\nScientific Operations:")
    print(" 1. sin(x)   [degrees]")
    print(" 2. cos(x)   [degrees]")
    print(" 3. tan(x)   [degrees]")
    print(" 4. log(x)   [base 10]")
    print(" 5. ln(x)    [natural]")
    choice = input("Choose an option: ").strip()

    # Trig functions require radians; degrees are converted first.
    if choice == "1":
        x = read_single_number("Enter angle in degrees: ")
        return math.sin(math.radians(x))
    elif choice == "2":
        x = read_single_number("Enter angle in degrees: ")
        return math.cos(math.radians(x))
    elif choice == "3":
        x = read_single_number("Enter angle in degrees: ")
        return math.tan(math.radians(x))
    elif choice == "4":
        x = read_single_number("Enter a positive number: ")
        if x <= 0:
            return "Error: log is defined only for positive numbers"
        return math.log10(x)
    elif choice == "5":
        x = read_single_number("Enter a positive number: ")
        if x <= 0:
            return "Error: ln is defined only for positive numbers"
        return math.log(x)
    else:
        return "Error: Invalid scientific operation"


# ---------------------------------------------------------------------------
# UTILITY FUNCTIONS
# ---------------------------------------------------------------------------

def factorial(num):
    """
    Return the factorial of a non-negative integer using an iterative loop.
    Non-integer or negative inputs produce an error message.
    """
    if num < 0:
        return "Error: Factorial of a negative number is undefined"
    if num != int(num):
        return "Error: Factorial is defined only for integers"
    num = int(num)
    answer = 1
    for i in range(1, num + 1):
        answer *= i
    return answer


def gcd_lcm():
    """
    Compute the Greatest Common Divisor and the Least Common Multiple
    of two integers.
    """
    a = int(read_single_number("Enter first integer: "))
    b = int(read_single_number("Enter second integer: "))
    g = math.gcd(a, b)
    # LCM is derived from the GCD relationship: |a * b| / gcd(a, b).
    l = abs(a * b) // g if g != 0 else 0
    return f"GCD = {g}, LCM = {l}"


def is_prime():
    """
    Determine whether an integer is prime.
    Only odd divisors up to the square root of the number are tested.
    """
    n = int(read_single_number("Enter an integer: "))
    if n < 2:
        return f"{n} is not a prime number"
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return f"{n} is not a prime number"
    return f"{n} is a prime number"


def complex_arithmetic():
    """
    Perform complex arithmetic (+, -, *, /) on complex numbers.
    Each complex number is entered as two consecutive values: real, imaginary.
    """
    print("\nComplex Arithmetic:")
    print(" 1. Addition")
    print(" 2. Subtraction")
    print(" 3. Multiplication (exactly 2 complex numbers)")
    print(" 4. Division (exactly 2 complex numbers)")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        nums = list(map(float, input("Enter pairs (real imag ...): ").split()))
        real = sum(nums[0::2])
        imag = sum(nums[1::2])
        return f"{real} + i{imag}"

    elif choice == "2":
        nums = list(map(float, input("Enter pairs (real imag ...): ").split()))
        real = nums[0] - sum(nums[2::2])
        imag = nums[1] - sum(nums[3::2])
        return f"{real} + i{imag}"

    elif choice == "3":
        nums = list(map(float, input("Enter 4 numbers (a b c d): ").split()))
        if len(nums) != 4:
            return "Error: Multiplication needs exactly 4 numbers"
        a, b, c, d = nums
        # (a + bi)(c + di) = (ac - bd) + (ad + bc)i
        real = a * c - b * d
        imag = a * d + b * c
        return f"{real} + i{imag}"

    elif choice == "4":
        nums = list(map(float, input("Enter 4 numbers (a b c d): ").split()))
        if len(nums) != 4:
            return "Error: Division needs exactly 4 numbers"
        a, b, c, d = nums
        denom = c ** 2 + d ** 2
        if denom == 0:
            return "Error: Division by zero complex number"
        # (a + bi)/(c + di) multiplied by the conjugate of the denominator.
        real = (a * c + b * d) / denom
        imag = (b * c - a * d) / denom
        return f"{real} + i{imag}"

    else:
        return "Error: Invalid complex operation"


def binomial():
    """
    Compute the binomial coefficient C(n, k) = n! / (k! * (n - k)!).
    Requires 0 <= k <= n.
    """
    nums = list(map(int, input("Enter n and k separated by space: ").split()))
    if len(nums) != 2:
        return "Error: Please enter exactly two integers"
    n, k = nums
    if n < 0 or k < 0 or k > n:
        return "Error: Requires 0 <= k <= n"
    return factorial(n) / (factorial(k) * factorial(n - k))


# ---------------------------------------------------------------------------
# MEMORY & HISTORY OPERATIONS
# ---------------------------------------------------------------------------

def memory_operation():
    """
    Manage the persistent memory register.
    M+ adds a value, M- subtracts a value, MR recalls, MC clears.
    """
    global memory

    print("\nMemory Operations:")
    print(" 1. M+  (add value to memory)")
    print(" 2. M-  (subtract value from memory)")
    print(" 3. MR  (recall memory)")
    print(" 4. MC  (clear memory)")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        value = read_single_number("Enter value to add to memory: ")
        memory += value
        return f"Memory = {memory}"
    elif choice == "2":
        value = read_single_number("Enter value to subtract from memory: ")
        memory -= value
        return f"Memory = {memory}"
    elif choice == "3":
        return f"Memory = {memory}"
    elif choice == "4":
        memory = 0.0
        return "Memory cleared"
    else:
        return "Error: Invalid memory operation"


def show_history():
    """Print every stored calculation along with an ordinal number."""
    if not history:
        return "No history yet"
    print("\n--- Calculation History ---")
    for i, entry in enumerate(history, 1):
        print(f"{i}. {entry}")
    return f"({len(history)} entries shown)"


# ---------------------------------------------------------------------------
# MAIN MENU LOOP
# ---------------------------------------------------------------------------

def print_menu():
    """Print the list of available operations."""
    print("\n===== ADVANCED CALCULATOR =====")
    print(" 1. Addition")
    print(" 2. Subtraction")
    print(" 3. Multiplication")
    print(" 4. Division")
    print(" 5. Average")
    print(" 6. Factorial")
    print(" 7. Complex Arithmetic")
    print(" 8. Binomial Coefficient")
    print(" 9. Power (x^y)")
    print("10. Square Root")
    print("11. Modulus (remainder)")
    print("12. Percentage")
    print("13. Scientific Functions (sin/cos/tan/log/ln)")
    print("14. GCD & LCM")
    print("15. Prime Check")
    print("16. Memory Operations")
    print("17. Show History")
    print(" 0. Exit")


def main():
    """Run the calculator loop until the user chooses to exit."""
    while True:
        print_menu()
        choice = input("Your choice: ").strip()
        expression = ""
        result = None

        try:
            if choice == "1":
                result = addition()
                expression = "addition"
            elif choice == "2":
                result = subtraction()
                expression = "subtraction"
            elif choice == "3":
                result = multiplication()
                expression = "multiplication"
            elif choice == "4":
                result = division()
                expression = "division"
            elif choice == "5":
                result = average()
                expression = "average"
            elif choice == "6":
                n = read_single_number("Enter the number: ")
                result = factorial(n)
                expression = f"{int(n)}!"
            elif choice == "7":
                result = complex_arithmetic()
                expression = "complex"
            elif choice == "8":
                result = binomial()
                expression = "binomial"
            elif choice == "9":
                result = power()
                expression = "power"
            elif choice == "10":
                result = square_root()
                expression = "sqrt"
            elif choice == "11":
                result = modulus()
                expression = "modulus"
            elif choice == "12":
                result = percentage()
                expression = "percentage"
            elif choice == "13":
                result = scientific()
                expression = "scientific"
            elif choice == "14":
                result = gcd_lcm()
                expression = "gcd/lcm"
            elif choice == "15":
                result = is_prime()
                expression = "prime check"
            elif choice == "16":
                result = memory_operation()
                expression = "memory"
            elif choice == "17":
                result = show_history()
                expression = "history"
            elif choice == "0":
                print("Thank you for using the calculator! Goodbye 👋")
                break
            else:
                print("Sorry, invalid option!")
                continue

            # Display the result and store it in history.
            print(f"The answer is: {result}")
            log_history(expression, result)

        except ValueError:
            print("Invalid input! Please enter numeric values only.")
        except Exception as err:
            # Prevents a single unexpected input from terminating the loop.
            print(f"Unexpected error: {err}")

        # Brief pause so the user can read the output before the menu returns.
        time.sleep(1)


if __name__ == "__main__":
    main()
