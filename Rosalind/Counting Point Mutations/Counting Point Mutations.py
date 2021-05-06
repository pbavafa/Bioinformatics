'''
Problem
Figure 2. The Hamming distance between these two strings is 7. Mismatched symbols are colored red.

Given two strings s
and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t. See Figure 2.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t)
'''

def CountingPointMutations(s,t): #s and t represent strings of equal length
    if s == t:
        return 0
    else:
        return len(list(filter(lambda x: x[0] != x[1], zip(s, t))))

with open("C:\\Users\\pouya\\Documents\\Python-Projects\\Bioinformatics\\Rosalind\\Counting Point Mutations\\rosalind_hamm.txt", "r") as DnaStrings:
    DnaString = DnaStrings.read().split()
    s = DnaString[0]
    t = DnaString[1]

print(CountingPointMutations(s,t))