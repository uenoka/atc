# Mendels_First_Law.py
def mendel(dominant, hetero, recessive):
    total = dominant + hetero + recessive
    twoRecess = (recessive/total)*((recessive-1)/(total-1))
    twoHetero = (hetero/total)*((hetero-1)/(total-1))
    heteroRecess = (recessive/total)*(hetero/(total-1)) + (hetero/total)*(recessive/(total-1))
    recessProb = twoRecess + twoHetero*1/4 + heteroRecess*1/2
    print(1-recessProb)  # take the complement


with open("./rosalind_iprb.txt", "r") as file:
    line = file.readline().split()
    x, y, z = [int(n) for n in line]
    print(x, y, z)
file.close()
mendel(x, y, z)
