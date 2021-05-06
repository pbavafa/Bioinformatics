'''
Problem

A permutation of length n
is an ordering of the positive integers {1,2,…,n}. 
For example, π=(5,3,2,1,4) is a permutation of length 5.

Given: A positive integer n≤7.

Return: The total number of permutations of length n, 
followed by a list of all such permutations (in any order).
'''

from itertools import permutations  
def EnumeratingGeneOrders(int):
    list = []
    for i in range(int):
        list.append(i)
    # Get all permutations
    perm = permutations(list)  

    # Print the obtained permutations  
    for i in perm:  
        print (i)  

print(EnumeratingGeneOrders(3))
