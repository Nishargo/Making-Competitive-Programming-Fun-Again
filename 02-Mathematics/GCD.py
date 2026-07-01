"""
GCD (Greatest Common Divisor) using Euclid’s Algorithm

-------------------------------------------------------
PROBLEM
-------------------------------------------------------
Find the greatest number that divides both a and b.

Example:
GCD(48, 18) = 6

-------------------------------------------------------
KEY IDEA (EUCLID'S INSIGHT)
-------------------------------------------------------
Instead of checking all divisors, we use:

GCD(a, b) = GCD(b, a % b)

Why does this work?

Because:
a = (b × q) + r
⇒ r = a - (b × q)

Any number that divides both a and b must also divide r. So we safely replace (a, b) → (b, r) without changing the answer. This reduces the problem size until b becomes 0.
"""

def gcd(a, b):
    """
    Euclidean Algorithm for GCD

    We repeatedly replace:
        (a, b) → (b, a % b)
    until b becomes 0.
    """
    while b != 0:

        # -----------------------------
        # TUPLE UNPACKING EXPLAINED
        # -----------------------------
        """
        This line:
            a, b = b, a % b

        is NOT two separate assignments.

        Python does this in 2 steps:

        1. Evaluate right-hand side first:
            temp = (b, a % b)

        2. Assign simultaneously:
            a = temp[0]
            b = temp[1]

        Why this matters:
        If we wrote:
            a = b
            b = a % b   WRONG

        then 'a' would already be changed before computing b.

        Tuple unpacking avoids this bug by updating both values at once.
        """

        a, b = b, a % b

    return a


# -----------------------------
# STEP-BY-STEP EXAMPLE
# -----------------------------
"""
Let’s compute GCD(48, 18)

Step 1:
48 = (18 × 2) + 12
→ (a, b) = (18, 12)

Step 2:
18 = (12 × 1) + 6
→ (a, b) = (12, 6)

Step 3:
12 = (6 × 2) + 0
→ (a, b) = (6, 0)

Stop → GCD = 6
"""


# -----------------------------
# USER INPUT TEST
# -----------------------------
if __name__ == "__main__":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = gcd(num1, num2)

    print(f"\nGCD({num1}, {num2}) = {result}")
