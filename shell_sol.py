"""
Python Exercises: Practicing with Arithmetic Expressions,
Variables, and Functions
"""

"""
Experiment with the Python Shell
1. 9 / -2 = -4.5
2. 10 % 5 = 0
3. (6.25 - 0.5 ** 2) ** 2 % 9 + (125 + 50) / 25 * 8 = 56
4. a) 15 % -4 = -1
   b) -15 % 4 = 1
   c) -15 % -4 = -3
   d) 15 % 4 = 3
   The modulus function has the following formula:
    a % b = a - ((a // b) * b)
5. x = 0.0
6. x += x - x
   x = x + (x - x)
   x = x
   If x = 5, x = 5 after the statement is evaluated.
7. (See Python Programming #7)
8. i) "a" + 'b'
    Eval-
    "ab"
   ii) ("\tmi" + 'ssi' * 2 + "ppi" + "\n") * 3
    Eval-
        mississippi
        mississippi
        mississippi
"""

#Python Programming #7
def discriminant(a, b, c):
    return b ** 2 - 4 * a * c