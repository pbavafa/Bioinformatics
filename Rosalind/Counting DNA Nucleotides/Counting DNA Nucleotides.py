with open("rosalind_dna.txt", "r") as String:
    A = 0
    C = 0
    G = 0
    T = 0
    for letter in String.read():
        if letter == "A":
            A += 1
        elif letter == "C":
            C +=1
        elif letter == "G":
            G +=1
        elif letter == "T":
            T +=1

    print (A, C, G, T)

