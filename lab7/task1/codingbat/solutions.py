

def sleep_in(weekday: bool, vacation: bool) -> bool:
    """Return True if we can sleep in (not weekday OR vacation)."""
    return not weekday or vacation


def monkey_trouble(a_smile: bool, b_smile: bool) -> bool:
    """Trouble if both smiling or both not smiling."""
    return a_smile == b_smile


def sum_double(a: int, b: int) -> int:
    """Return a+b, doubled if a==b."""
    total = a + b
    return total * 2 if a == b else total


def diff21(n: int) -> int:
    """Absolute diff from 21, doubled if n > 21."""
    diff = abs(21 - n)
    return diff * 2 if n > 21 else diff


def parrot_trouble(talking: bool, hour: int) -> bool:
    """Trouble if parrot talking before 7 or after 20."""
    return talking and (hour < 7 or hour > 20)


def makes10(a: int, b: int) -> bool:
    """True if one is 10 or a+b==10."""
    return a == 10 or b == 10 or a + b == 10


def near_hundred(n: int) -> bool:
    """True if within 10 of 100 or 200."""
    return abs(100 - n) <= 10 or abs(200 - n) <= 10


def pos_neg(a: int, b: int, negative: bool) -> bool:
    """Both negative if flag, else one negative one positive."""
    if negative:
        return a < 0 and b < 0
    return (a < 0) != (b < 0)


def not_string(s: str) -> str:
    """Add 'not ' in front unless already starts with 'not'."""
    return s if s.startswith("not") else "not " + s


def missing_char(s: str, n: int) -> str:
    """Return string with char at index n removed."""
    return s[:n] + s[n + 1:]


def front_back(s: str) -> str:
    """Swap first and last characters."""
    if len(s) <= 1:
        return s
    return s[-1] + s[1:-1] + s[0]


def front3(s: str) -> str:
    """Return first 3 chars of s repeated 3 times."""
    front = s[:3]
    return front * 3


# ================================================================
# WARMUP-2
# ================================================================

def string_times(s: str, n: int) -> str:
    return s * n


def front_times(s: str, n: int) -> str:
    return s[:3] * n


def string_bits(s: str) -> str:
    return s[::2]


def string_splosion(s: str) -> str:
    return "".join(s[:i + 1] for i in range(len(s)))


def last2(s: str) -> int:
    """Count occurrences of last 2 chars in the rest of the string."""
    if len(s) < 2:
        return 0
    end = s[-2:]
    count = 0
    for i in range(len(s) - 2):
        if s[i:i + 2] == end:
            count += 1
    return count


def array_count9(nums: list) -> int:
    return nums.count(9)


def array_front9(nums: list) -> bool:
    return 9 in nums[:4]


def array123(nums: list) -> bool:
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
            return True
    return False


def string_match(a: str, b: str) -> int:
    shorter = min(len(a), len(b))
    return sum(1 for i in range(shorter - 1) if a[i:i + 2] == b[i:i + 2])


# ================================================================
# STRING-1
# ================================================================

def hello_name(name: str) -> str:
    return f"Hello {name}!"


def make_abba(a: str, b: str) -> str:
    return a + b + b + a


def make_tags(tag: str, word: str) -> str:
    return f"<{tag}>{word}</{tag}>"


def make_out_word(out: str, word: str) -> str:
    return out[:2] + word + out[2:]


def extra_end(s: str) -> str:
    return s[-2:] * 3


def first_two(s: str) -> str:
    return s[:2]


def first_half(s: str) -> str:
    return s[:len(s) // 2]


def without_end(s: str) -> str:
    return s[1:-1]


def combo_string(a: str, b: str) -> str:
    shorter, longer = (a, b) if len(a) <= len(b) else (b, a)
    return shorter + longer + shorter


def non_start(a: str, b: str) -> str:
    return a[1:] + b[1:]


def left2(s: str) -> str:
    return s[2:] + s[:2]


# ================================================================
# STRING-2
# ================================================================

def count_hi(s: str) -> int:
    return s.count("hi")


def cat_dog(s: str) -> bool:
    return s.count("cat") == s.count("dog")


def count_code(s: str) -> int:
    count = 0
    for i in range(len(s) - 3):
        if s[i:i + 2] == "co" and s[i + 3] == "e":
            count += 1
    return count


def end_other(a: str, b: str) -> bool:
    a, b = a.lower(), b.lower()
    return a.endswith(b) or b.endswith(a)


def xyz_there(s: str) -> bool:
    for i in range(len(s) - 2):
        if s[i:i + 3] == "xyz" and (i == 0 or s[i - 1] != "."):
            return True
    return False


# ================================================================
# LIST-1
# ================================================================

def first_last6(nums: list) -> bool:
    return nums[0] == 6 or nums[-1] == 6


def same_first_last(nums: list) -> bool:
    return len(nums) >= 1 and nums[0] == nums[-1]


def make_pi() -> list:
    return [3, 1, 4]


def common_end(a: list, b: list) -> bool:
    return a[0] == b[0] or a[-1] == b[-1]


def sum3(nums: list) -> int:
    return sum(nums)


def rotate_left3(nums: list) -> list:
    return nums[1:] + nums[:1]


def reverse3(nums: list) -> list:
    return nums[::-1]


def max_end3(nums: list) -> list:
    m = max(nums[0], nums[-1])
    return [m, m, m]


def sum2(nums: list) -> int:
    return sum(nums[:2])


def middle_way(a: list, b: list) -> list:
    return [a[1], b[1]]


def make_ends(nums: list) -> list:
    return [nums[0], nums[-1]]


def has23(nums: list) -> bool:
    return 2 in nums or 3 in nums


# ================================================================
# LIST-2
# ================================================================

def count_evens(nums: list) -> int:
    return sum(1 for n in nums if n % 2 == 0)


def big_diff(nums: list) -> int:
    return max(nums) - min(nums)


def centered_average(nums: list) -> int:
    s = sorted(nums)
    return sum(s[1:-1]) // len(s[1:-1])


def sum13(nums: list) -> int:
    total = 0
    i = 0
    while i < len(nums):
        if nums[i] == 13:
            i += 2
        else:
            total += nums[i]
            i += 1
    return total


def sum67(nums: list) -> int:
    total = 0
    skip = False
    for n in nums:
        if n == 6:
            skip = True
        elif n == 7 and skip:
            skip = False
        elif not skip:
            total += n
    return total


def has22(nums: list) -> bool:
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i + 1] == 2:
            return True
    return False


# ================================================================
# DEMO
# ================================================================
if __name__ == "__main__":
    # Warmup-1
    print("sleep_in(False, False):", sleep_in(False, False))   # True
    print("sum_double(3, 3):", sum_double(3, 3))               # 12
    print("diff21(19):", diff21(19))                           # 2
    print("front3('Chocolate'):", front3("Chocolate"))         # ChoCho Cho

    # Warmup-2
    print("string_bits('Hello'):", string_bits("Hello"))       # Hlo
    print("array123([1,1,2,3,1]):", array123([1, 1, 2, 3, 1]))# True

    # String-1
    print("make_tags('i','Yay'):", make_tags("i", "Yay"))      # <i>Yay</i>
    print("left2('Hello'):", left2("Hello"))                   # lloHe

    # String-2
    print("count_hi('hi ho hi'):", count_hi("hi ho hi"))       # 2
    print("cat_dog('catdog'):", cat_dog("catdog"))             # True

    # List-1
    print("rotate_left3([1,2,3]):", rotate_left3([1, 2, 3]))   # [2,3,1]
    print("has23([4,5]):", has23([4, 5]))                      # False

    # List-2
    print("count_evens([2,1,2,3,4]):", count_evens([2, 1, 2, 3, 4]))  # 3
    print("sum13([1,2,2,1]):", sum13([1, 2, 2, 1]))                    # 6
    print("sum67([1,2,2,7,7]):", sum67([1, 2, 2, 7, 7]))               # 5
