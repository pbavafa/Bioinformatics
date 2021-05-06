with open("C:\\Users\\pouya\\Documents\\Python-Projects\\Bioinformatics\\Rosalind\\Rabbits and Recurrence Relations\\rosalind_fib.txt", "r") as nk:
    nk = nk.read()
    nk = nk.split() #Split numbers by spaces
    
    n = int(nk[0])
    k = int(nk[1])
    ini = [1, 1]
    for i in range(n-2):
        ini.append(ini[i] * k + ini[i+1])

    print(ini[-1])
