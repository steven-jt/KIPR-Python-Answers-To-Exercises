import random

def make_random_code():
    color_opt = ['R', 'G', 'B', 'Y', 'O', 'W']
    str = ""
    for i in range(4):
        str += random.choice(color_opt)
    return str

def count_exact_matches(ls1, ls2):
    count = 0
    if len(ls1) == len(ls2):
        for i in range(len(ls1)):
            if ls1[i] == ls2[i]:
                count = count + 1
    return count

def count_letter_matches(ls1, ls2):
    count = 0
    if len(ls1) == len(ls2):
        for i in range(len(ls1)):
            if ls1[i] in ls2:
                count += 1
    return count

def compare_codes(str1, str2):
    exact = count_exact_matches(str1, str2)
    letter = count_letter_matches(str1, str2)
    blank = 4 - (exact + letter)
    return ("B" * exact + "W" * letter + "-" * blank)[0:4]

def new_game():
    print("New Game")
    secret_code = make_random_code()
    res = ""
    n = 0
    print("SECRET CODE: ", secret_code)
    while res != 'BBBB':
        user = input("Enter your guess: ")
        res = compare_codes(user, secret_code)
        print("Result: ", res)
        n += 1
    print("Congratulations! You cracked the code in %d moves!" % n)
