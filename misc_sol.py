import math, random

def product(num_ls):
    product = 1
    for num in num_ls:
        product *= num
    return product

def factorial(n):
    n = int(n)
    factors = range(1, n + 1)
    return product(factors)

def dice(sides, num_of_dice):
    die = range(1, sides + 1)
    sum = 0
    for i in range(num_of_dice):
        sum += random.choice(die)
    return sum

def remove_all(ls, n):
    while n in ls:
        ls.remove(n)
        print(ls)

def any_in(ls_1, ls_2):
    lst = ls_1
    o_lst = ls_2
    if len(ls_1) > len(ls_2):
        lst = ls_2
        o_lst = ls_1
    for n in lst:
        if n in o_lst:
            return True
    return False

def isFactorish(n):
    if type(n) != int:
        return False
    n = abs(n)
    n_1 = int(n % 10)
    n_10 = int(n % 100 / 10)
    n_100 = int(n % 1000 / 100)
    is_unique = n_1 != n_10 and n_10 != n_100 and n_1 != n_100
    is_nonzero = n_1 != 0 and n_10 != 0 and n_100 != 0
    is_three_digits = not((n / 1000) > 1)
    if is_unique and is_three_digits and is_nonzero:
        return n % n_1 == 0 and n % n_10 == 0 and n % n_100 == 0
    return False

#2
def threeLinesArea(m1, b1, m2, b2, m3, b3):
    x1 = determine_intersection(m1, b1, m2, b2)
    x2 = determine_intersection(m2, b2, m3, b3)
    x3 = determine_intersection(m1, b1, m3, b3)
    y1 = m1 * x1 + b1
    y2 = m2 * x2 + b2
    y3 = m3 * x3 + b3
    a = dist(x1, y1, x2, y2)
    b = dist(x2, y2, x3, y3)
    c = dist(x1, y1, x3, y3)
    return herons(a, b, c)

def determine_intersection(m1, b1, m2, b2):
    return (b2 - b1) / (m1 - m2)

def dist(x1, y1, x2, y2):
    return math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)

def herons(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

#3

def roundUp(n):
    if type(n) == float or type(n) == int:
        decimals = n - int(n)
        if decimals >= 0.5:
            return int(n) + 1
        return int(n)
    return None

def colorBlender(rgb1, rgb2, midpoints, n):
    RED = 0
    GREEN = 1
    BLUE = 2
    r_1 = getColorNum(rgb1, RED)
    g_1 = getColorNum(rgb1, GREEN)
    b_1 = getColorNum(rgb1, BLUE)
    r_2 = getColorNum(rgb2, RED)
    g_2 = getColorNum(rgb2, GREEN)
    b_2 = getColorNum(rgb2, BLUE)
    width_r = roundUp((r_2 - r_1) / (midpoints + 1))
    width_g = roundUp((g_2 - g_1) / (midpoints + 1))
    width_b = roundUp((b_2 - b_1) / (midpoints + 1))
    red = r_1 + width_r * n
    green = g_1 + width_g * n
    blue = b_1 + width_b * n
    return blue + green * 1000 + red * 1000000

def getColorNum(rgb, segment):
    return int((rgb / 1000 ** (2 - segment)) % 1000)

def list_reverse(lst):
    lim = len(lst) // 2
    if lim != 0:
        for index in range(0, lim + 1):
            temp = lst[index]
            lst[index] = lst[len(lst) - (1 + index)]
            lst[len(lst) - (1 + index)] = temp

def binary_to_decimal(bin):
    bin = list(bin)
    index = range(-1, -(len(bin) + 1), -1)
    res = 0
    for n in index:
        res += int(bin[n]) * (2 ** ((len(bin) - 1) - (-index[n] - 1)))
    return res

def decimal_to_binary(dec_num):
    if dec_num == 0:
        return [dec_num]
    num_of_digit = math.log(dec_num, 2)
    digits = [0] * (int(num_of_digit) + 1)
    while dec_num > 0:
        num_of_digit = int(math.log(dec_num, 2))
        digits[len(digits) - int(num_of_digit) - 1] = 1
        dec_num -= 2 ** int(num_of_digit)
    return digits