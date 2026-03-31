# ============================================================
# Informatics.msk.ru — Python Solutions
# ============================================================

# ----------------------------------------------------------------
# INPUT / OUTPUT & ASSIGNMENT OPERATORS — Problems A–E
# ----------------------------------------------------------------

# Problem A: Read two integers and print their sum
def io_a():
    a, b = map(int, input().split())
    print(a + b)


# Problem B: Read a float and print it rounded to 2 decimal places
def io_b():
    x = float(input())
    print(f"{x:.2f}")


# Problem C: Swap two variables and print them
def io_c():
    a, b = map(int, input().split())
    a, b = b, a
    print(a, b)


# Problem D: Read three numbers and print their product
def io_d():
    a, b, c = map(int, input().split())
    print(a * b * c)


# Problem E: Read a number and print its square and cube
def io_e():
    n = int(input())
    print(n ** 2, n ** 3)


# ----------------------------------------------------------------
# CONDITIONAL STATEMENTS — Problems A–E
# ----------------------------------------------------------------

# Problem A: Check if a number is positive, negative, or zero
def cond_a():
    n = int(input())
    if n > 0:
        print("positive")
    elif n < 0:
        print("negative")
    else:
        print("zero")


# Problem B: Find the maximum of two numbers
def cond_b():
    a, b = map(int, input().split())
    print(a if a > b else b)


# Problem C: Check if a number is even or odd
def cond_c():
    n = int(input())
    print("even" if n % 2 == 0 else "odd")


# Problem D: Grade classifier (A/B/C/D/F)
def cond_d():
    score = int(input())
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("F")


# Problem E: Leap year check
def cond_e():
    year = int(input())
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("leap")
    else:
        print("not leap")


# ----------------------------------------------------------------
# LOOPS: FOR LOOP — Problems A–M
# ----------------------------------------------------------------

# Problem A: Print numbers 1 to N
def for_a():
    n = int(input())
    for i in range(1, n + 1):
        print(i)


# Problem B: Sum of numbers from 1 to N
def for_b():
    n = int(input())
    print(sum(range(1, n + 1)))


# Problem C: Print multiplication table for N
def for_c():
    n = int(input())
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")


# Problem D: Print even numbers from 1 to N
def for_d():
    n = int(input())
    for i in range(2, n + 1, 2):
        print(i)


# Problem E: Factorial of N
def for_e():
    n = int(input())
    result = 1
    for i in range(2, n + 1):
        result *= i
    print(result)


# Problem F: Count digits of a number
def for_f():
    n = input().strip()
    print(len(n.replace("-", "")))


# Problem G: Sum of digits of a number
def for_g():
    n = input().strip()
    print(sum(int(d) for d in n if d.isdigit()))


# Problem H: Reverse a number
def for_h():
    n = input().strip()
    print(n[::-1])


# Problem I: Check if a number is prime
def for_i():
    n = int(input())
    if n < 2:
        print("not prime")
        return
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print("not prime")
            return
    print("prime")


# Problem J: Fibonacci sequence up to N terms
def for_j():
    n = int(input())
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()


# Problem K: Print a right triangle of stars with N rows
def for_k():
    n = int(input())
    for i in range(1, n + 1):
        print("*" * i)


# Problem L: Count occurrences of a digit in a number
def for_l():
    n, d = input().split()
    print(n.count(d))


# Problem M: Print numbers divisible by both 3 and 5 up to N
def for_m():
    n = int(input())
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print(i)


# ----------------------------------------------------------------
# LOOPS: WHILE LOOP — Problems A–E
# ----------------------------------------------------------------

# Problem A: Sum digits until the number becomes 0
def while_a():
    n = int(input())
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    print(total)


# Problem B: Collatz conjecture — steps to reach 1
def while_b():
    n = int(input())
    steps = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    print(steps)


# Problem C: Read numbers until 0, print their sum
def while_c():
    total = 0
    while True:
        x = int(input())
        if x == 0:
            break
        total += x
    print(total)


# Problem D: Binary to decimal conversion
def while_d():
    binary = input().strip()
    decimal = 0
    power = 0
    for bit in reversed(binary):
        decimal += int(bit) * (2 ** power)
        power += 1
    print(decimal)


# Problem E: GCD using Euclidean algorithm
def while_e():
    a, b = map(int, input().split())
    while b:
        a, b = b, a % b
    print(a)


# ----------------------------------------------------------------
# ARRAYS (LISTS) — Problems A–G
# ----------------------------------------------------------------

# Problem A: Read N numbers into a list and print them reversed
def arr_a():
    n = int(input())
    lst = list(map(int, input().split()))
    print(*lst[::-1])


# Problem B: Find the minimum and maximum in a list
def arr_b():
    lst = list(map(int, input().split()))
    print(min(lst), max(lst))


# Problem C: Calculate the average of a list
def arr_c():
    lst = list(map(float, input().split()))
    print(f"{sum(lst) / len(lst):.2f}")


# Problem D: Count even and odd numbers in a list
def arr_d():
    lst = list(map(int, input().split()))
    evens = sum(1 for x in lst if x % 2 == 0)
    odds = len(lst) - evens
    print(f"even: {evens}, odd: {odds}")


# Problem E: Remove duplicates from a list (preserve order)
def arr_e():
    lst = list(map(int, input().split()))
    seen = []
    for x in lst:
        if x not in seen:
            seen.append(x)
    print(*seen)


# Problem F: Sort a list without using sort()  (bubble sort)
def arr_f():
    lst = list(map(int, input().split()))
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    print(*lst)


# Problem G: Second largest element in a list
def arr_g():
    lst = list(map(int, input().split()))
    unique = sorted(set(lst), reverse=True)
    print(unique[1] if len(unique) >= 2 else "N/A")


# ----------------------------------------------------------------
# FUNCTIONS — Problems A–C
# ----------------------------------------------------------------

# Problem A: Function to check palindrome
def is_palindrome(s: str) -> bool:
    s = s.lower().replace(" ", "")
    return s == s[::-1]


def func_a():
    word = input().strip()
    print("palindrome" if is_palindrome(word) else "not palindrome")


# Problem B: Function to count vowels in a string
def count_vowels(s: str) -> int:
    return sum(1 for c in s.lower() if c in "aeiou")


def func_b():
    s = input().strip()
    print(count_vowels(s))


# Problem C: Recursive function — power(base, exp)
def power(base: float, exp: int) -> float:
    if exp == 0:
        return 1
    if exp < 0:
        return 1 / power(base, -exp)
    return base * power(base, exp - 1)


def func_c():
    base, exp = map(int, input().split())
    print(power(base, exp))
