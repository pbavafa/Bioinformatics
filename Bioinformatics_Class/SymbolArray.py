def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(symbol, ExtendedGenome[i:i+(n//2)])
    return print(array)

def PatternCount(symbol, extended_genome):
    freq = 0

    n = len(extended_genome)
    k = len(symbol)
    for i in range(n-k+1):
        if Pattern == Text[i:i+k]: 
            freq += 1
    return freq
# with open("E_coli.txt", "r") as f:
#     Genome = f.read()
# symbol = "C"
# SymbolArray(Genome, symbol)
# print('hello')
# Genome = "AAAAGGGG"
# symbol = "A"
# SymbolArray(Genome, symbol)

Genome = "AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT"
symbol = "CC"
SymbolArray(Genome, symbol)
