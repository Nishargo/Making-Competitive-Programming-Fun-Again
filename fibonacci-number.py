# The Fibonacci Sequence is a series of numbers that has a pattern where the next number can be found by summing the two numbers before it.
Hee's an example:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,...

In the sequence above, We got 2 by adding the two numbers before it (1+1),
Then we got 3 by summing the two numbers before it (1+2),
We got 5 by adding 2+3
It goes on...

An exercise for you: find how we got 55 in the sequence?

Now, if we would like to make a rule out of it, we have to visualize it as a sequence:
n  =	0	1	2	3	4	5	6	7	8	9	10	11	12	13 ...
xn =	0	1	1	2	3	5	8	13	21	34	55	89	144 233...
Hence, term number 5 is called x5 (which equals 5).

Example: the 9th term is
the 8th term plus the 7th term:
x9 = x8 + x7

Fibonacci rule x9 = x8 + x7
Thus, the rule can be written as: 
xn = xn−1 + xn−2
where,
xn is term number "n"
xn−1 is the previous term (n−1)
xn−2 is the term before it (n−2)
Example: term 8 is calculated like this:
x8= x8−1 + x8−2
 = x7 + x6
 = 13 + 8
 = 21
   
We are going to create a function to find nth Fibonacci Number

We are going to consider 0 and 1 as the first two Fibonacci numbers

def fibonacci(n):
    x = 0
    y = 1
    if n < 0:
        print("Please insert a positive number.")
    elif n == 0:
        return x
    elif n == 1:
        return y
    else:
        for i in range(1, n):
            z = x + y
            x = y
            y = z
        return y
  
print(fibonacci(5))

Exercise: The Fibonacci sequence also works for terms below 0. Can you write a program for that?
