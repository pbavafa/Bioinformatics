# fill in your PatternMatching() function along with any subroutines that you need.
def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    n = len(Genome)
    k = len(Pattern)
    for i in range(n-k+1):
        if Genome[i:i+k] == Pattern:
            positions.append(i)
    return positions


Pattern = "ATAT"
Genome = "GATATATGCATATACTT"
PatternMatching(Pattern, Genome)