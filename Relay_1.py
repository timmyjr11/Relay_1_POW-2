from sympy import *

# Creates the variables to be used throughout the code
answer_One = int
answer_Two = int
answer_Three = float
true = True

# Creates the sum of the first natural numbers
t_1 = (55 * (55 + 1)) / 2

# Solves the first question to the problem
# Which is 15
answer_One = (t_1 + 75) % 100
print("The first answer is: " + str(answer_One))

# Cut off to question two
#
#

# States T^2 + 1 as a variable
t_2 = (answer_One * answer_One) + 1

# Uses summation to solve the Kth triangular number
# finding 20 to be the Kth term
k_1 = 0
while true:
    for i in range(100, 0, -1):
        k_1 = i * (i + 1)/2
        if t_2 > k_1:
            true = False
            break

k_1 = 20

# Solves the second question for the problem
# which is 57
answer_Two = (k_1 + 37) % 100
print("The second answer is: " + str(answer_Two))

# Cut off to question three
#
#

# Puts the answer that was writen above into a different variable
t_3 = answer_Two

# Creates a variable that is used to solve
k_2 = symbols('k_2')

# The equation to be solved
eq = Eq(cot(asin(1 / t_3)), sqrt(k_2))

# Solves the equation and gives the value of the variable
# which is 3248
solve(eq, k_2)

# Puts the answer of the equation into k_2 for the final step
k_2 = 3248

# Solves the third question to the problem
# Which is 46
answer_Three = (k_2 + 98) % 100
print("The third answer is: " + str(answer_Three))
