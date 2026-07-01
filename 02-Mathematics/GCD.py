"""
GCD (Greatest Common Divisor) using Euclid’s Algorithm

-------------------------------------------------------
🧠 PROBLEM
-------------------------------------------------------
Find the greatest number that divides both a and b exactly.

Example:
GCD(48, 18) = 6

-------------------------------------------------------
💡 KEY IDEA (EUCLID'S INSIGHT)
-------------------------------------------------------
Instead of checking all divisors, we use a mathematical property:

GCD(a, b) = GCD(b, a % b)

Why does this work?

Because:
a = b × q + r

So:
r = a - b × q

Any number that divides both a and b must also divide r.

👉 So the problem size reduces without changing the answer.

We keep shrinking the problem until remainder becomes 0.
"""

def gcd(a, b):
    """
    Euclidean Algorithm for GCD

    Repeatedly replace:
        (a, b) → (b, a % b)

    until b becomes 0.
    """
    while b != 0:
        a, b = b, a % b
    return a


# -----------------------------
# STEP-BY-STEP EXAMPLE
# -----------------------------
"""
Let’s compute GCD(48, 18)

Step 1:
48 = 18 × 2 + 12
→ (a, b) = (18, 12)

Step 2:
18 = 12 × 1 + 6
→ (a, b) = (12, 6)

Step 3:
12 = 6 × 2 + 0
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
