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
        complement += str(basepairs.get(char))
    return complement

with open('C:\\Users\\pouya\\Documents\\Python-Projects\\Bioinformatics\\Rosalind\\Complementing a Strand of DNA\\rosalind_revc.txt', 'r') as String:  
    String = String.read()
    result = ReverseComplement(String)
    print(result) 