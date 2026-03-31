   # ============================================================
# HackerRank — Python Domain Solutions (10 Problems)
# ============================================================

# ----------------------------------------------------------------
# 1. Say "Hello, World!" With Python
# ----------------------------------------------------------------
def hello_world():
    print("Hello, World!")


# ----------------------------------------------------------------
# 2. Python If-Else
#    If n is odd → print "Weird"
#    If n is even and 2 ≤ n ≤ 5  → "Not Weird"
#    If n is even and 6 ≤ n ≤ 20 → "Weird"
#    If n is even and n > 20      → "Not Weird"
# ----------------------------------------------------------------
def python_if_else(n: int) -> str:
    if n % 2 != 0:
        return "Weird"
    if 2 <= n <= 5:
        return "Not Weird"
    if 6 <= n <= 20:
        return "Weird"
    return "Not Weird"


# ----------------------------------------------------------------
# 3. Arithmetic Operators
#    Given a and b, print a+b, a-b, a*b on separate lines
# ----------------------------------------------------------------
def arithmetic_operators(a: int, b: int):
    print(a + b)
    print(a - b)
    print(a * b)


# ----------------------------------------------------------------
# 4. Python Division
#    Print integer division then float division
# ----------------------------------------------------------------
def python_division(a: int, b: int):
    print(a // b)
    print(a / b)


# ----------------------------------------------------------------
# 5. Loops
#    Print squares of 0..n-1
# ----------------------------------------------------------------
def loops_squares(n: int):
    for i in range(n):
        print(i ** 2)


# ----------------------------------------------------------------
# 6. Print Function
#    Print integers 1..n concatenated without spaces
# ----------------------------------------------------------------
def print_function(n: int):
    print("".join(str(i) for i in range(1, n + 1)))


# ----------------------------------------------------------------
# 7. List Comprehensions
#    Generate all (x,y,z) where x+y != z, for ranges [0,X],[0,Y],[0,Z]
# ----------------------------------------------------------------
def list_comprehensions(x: int, y: int, z: int, n: int) -> list:
    return [[i, j, k]
            for i in range(x + 1)
            for j in range(y + 1)
            for k in range(z + 1)
            if i + j != n]


# ----------------------------------------------------------------
# 8. Find the Runner-Up Score
#    Given a list of scores, find the second maximum
# ----------------------------------------------------------------
def runner_up_score(scores: list) -> int:
    unique = sorted(set(scores))
    return unique[-2]


# ----------------------------------------------------------------
# 9. Nested Lists
#    Given names and grades, print names of students with
#    the second lowest grade, sorted alphabetically
# ----------------------------------------------------------------
def nested_lists(students: list) -> list:
    grades = sorted(set(s[1] for s in students))
    second_lowest = grades[1]
    result = sorted(s[0] for s in students if s[1] == second_lowest)
    return result


# ----------------------------------------------------------------
# 10. Finding the Percentage
#     Given a dict of name→[marks], print average of a queried name
#     formatted to 2 decimal places
# ----------------------------------------------------------------
def finding_percentage(record: dict, query: str) -> str:
    avg = sum(record[query]) / len(record[query])
    return f"{avg:.2f}"


# ================================================================
# DEMO
# ================================================================
if __name__ == "__main__":
    print("=== 1. Hello World ===")
    hello_world()

    print("\n=== 2. If-Else ===")
    for n in [3, 4, 6, 24]:
        print(f"n={n}: {python_if_else(n)}")

    print("\n=== 3. Arithmetic Operators (a=3, b=5) ===")
    arithmetic_operators(3, 5)

    print("\n=== 4. Division (a=4, b=3) ===")
    python_division(4, 3)

    print("\n=== 5. Squares up to n=5 ===")
    loops_squares(5)

    print("\n=== 6. Print Function n=5 ===")
    print_function(5)

    print("\n=== 7. List Comprehensions X=1,Y=1,Z=1,n=2 ===")
    print(list_comprehensions(1, 1, 1, 2))

    print("\n=== 8. Runner-Up Score ===")
    print(runner_up_score([2, 3, 6, 6, 5]))

    print("\n=== 9. Nested Lists ===")
    students = [["Harry", 37.21], ["Berry", 37.21], ["Tina", 37.2],
                ["Akriti", 41], ["Harsh", 39]]
    print(nested_lists(students))

    print("\n=== 10. Finding the Percentage ===")
    record = {"Krishna": [67, 68, 69], "Arjun": [70, 98, 63], "Malika": [52, 56, 60]}
    print(finding_percentage(record, "Malika"))
