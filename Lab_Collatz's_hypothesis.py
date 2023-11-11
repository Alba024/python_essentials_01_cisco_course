# In 1937, a German mathematician named Lothar Collatz formulated an intriguing hypothesis 
# (it still remains unproven) which can be described in the following way:
# 1. Take any non-negative and non-zero integer number and name it c0;
# 2. If it's even, evaluate a new c0 as c0 ÷ 2;
# 3. Otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
# 4. If c0 ≠ 1, go back to point 2.
## The hypothesis says that regardless of the initial value of c0, it will always go to 1.##
########################################################################
# Write a program which reads one natural number and executes the above steps as 
# long as c0 remains different from 1.
# The code should output all the intermediate values of c0, too.
# The most important part of the problem is how to transform Collatz's idea into
# a while loop – this is the key to success.

c0 = int(input("Enter a non-negative, non-zero integer: "))
counter = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 //= 2
    else:
        c0 = 3 * c0 + 1
    print(c0)
    counter += 1

print("steps=", counter) 
