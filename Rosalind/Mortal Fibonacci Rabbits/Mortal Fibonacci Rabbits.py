'''
Problem
Figure 4. A figure illustrating the propagation of Fibonacci's rabbits if they die after three months.

Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence Relations”, which followed the recurrence relation Fn=Fn−1+Fn−2

and assumed that each pair of rabbits reaches maturity in one month and produces a single pair of offspring (one male, one female) each subsequent month.

Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all rabbits die out after a fixed number of months. See Figure 4 for a depiction of a rabbit tree in which rabbits live for three months (meaning that they reproduce only twice before dying).

Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.
'''

def MortalFibonacciRabbits(month, lifespan):
    """
    history[month] = (num_adults,num_children)
    """
    a, c = 0, 1  # first month, 1 child no adults
    h = [(a, c)]
    for m in range(1, month):
        c = h[m - 1][0]  # number of children ALWAYS is the number of adults alive previous month
        a = h[m - 1][0] + h[m - 1][1]  # number of adults is number of adults and children from previous month
        if m >= lifespan:
            a -= h[m - lifespan][1]  # minus number of children that were alive a lifespan ago (children back then are now dead)
        h.append((a, c))  # save to history
    # print(h)
    return sum(h[-1])  # sum of adults and children


print(MortalFibonacciRabbits(86,19))








