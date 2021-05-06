# Copy your PatternCount function below here
def PatternCount(Text, Pattern):
    freq = 0
    n = len(Text)
    k = len(Pattern)
    for i in range(n-k+1):
        if Pattern == Text[i:i+k]:
            freq += 1
            print(freq)
    return freq

# On the following line, create a variable called Text that is equal to the oriC region from T petrophila
Text = "AACTCTATACCTCCTTTTTGTCGAATTTGTGTGATTTATAGAGAAAATCTTATTAACTGAAACTAAAATGGTAGGTTTGGTGGTAGGTTTTGTGTACATTTTGTAGTATCTGATTTTTAATTACATACCGTATATTGTATTAAATTGACGAACAATTGCATGGAATTGAATATATGCAAAACAAACCTACCACCAAACTCTGTATTGACCATTTTAGGACAACTTCAGGGTGGTAGGTTTCTGAAGCTCTCATCAATAGACTATTTTAGTCTTTACAAACAATATTACCGTTCAGATTCAAGATTCTACAACGCTGTTTTAATGGGCGTTGCAGAAAACTTACCACCTAAAATCCAGTATCCAAGCCGATTTCAGAGAAACCTACCACTTACCTACCACTTACCTACCACCCGGGTGGTAAGTTGCAGACATTATTAAAAACCTCATCAGAAGCTTGTTCAAAAATTTCAATACTCGAAACCTACCACCTGCGTCCCCTATTATTTACTACTACTAATAATAGCAGTATAATTGATCTGA"

# On the following line, create a variable called count_1 that is equal to the number of times
# that "ATGATCAAG" occurs in Text.
count_1 = PatternCount(Text, "ATGATCAAG")

# On the following line, create a variable called count_2 that is equal to the number of times
# that "CTTGATCAT" occurs in Text. 
count_2 = PatternCount(Text, "CTTGATCAT")

# Finally, print the sum of count_1 and count_2
print(count_1 + count_2)