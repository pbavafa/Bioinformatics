def ReverseComplement(Pattern):
    Pattern = Reverse(Pattern) # reverse all letters in a string
    Pattern = Complement(Pattern) # complement each letter in a string
    return Pattern

def Reverse(Pattern):
    return Pattern[::-1]

def Complement(Pattern):
    basepairs = {"A":"T", "G":"C", "T":"A", "C":"G"}
    complement = ""
    for char in Pattern:
        complement += basepairs.get(char)
    return complement

# ReverseComplement('AAAACCCGGT')
result = Complement('AAAACCCGGT')
print(result) 