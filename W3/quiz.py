import numpy as np
from median_string import median_string

# 3

def calculate_entropy(distro: list) -> float:
    entropy = 0
    for el in distro:
        entropy -= el * np.log2(el)
    
    return entropy

print(calculate_entropy([0.5, 1, 1, 0.5]))
print(calculate_entropy([0.25, 0.25, 0.25, 0.25]))
print(calculate_entropy([1, 1, 1, 1]))
print(calculate_entropy([0.25, 1, 0.5, 0.25]))

# 5 
dna = [
    "CTCGATGAGTAGGAAAGTAGTTTCACTGGGCGAACCACCCCGGCGCTAATCCTAGTGCCC",
    "GCAATCCTACCCGAGGCCACATATCAGTAGGAACTAGAACCACCACGGGTGGCTAGTTTC",
    "GGTGTTGAACCACGGGGTTAGTTTCATCTATTGTAGGAATCGGCTTCAAATCCTACACAG"
]
k = 7

med_str = median_string(dna, k)

print(med_str)

# 6

print(0.1*0.3*1*0.4*0.5*0.9)


