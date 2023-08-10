"""
Task:
Find a DnaA box in Salmonella Enterica.
"""

from freq_mismatch_reverse_compliments import freq_mismatch_reverse_compliments
from minimum_skew import minimum_skew

def find_dnaa_box(genome: str) -> str:
    """
    Finds the possible dnaa boxes of genome by finding the 
    most frequent 9-mers with mismatches and
    reverse compliment in the region suggested by the
    minimum skew as ori
    """
    # Find ori
    min_skews = minimum_skew(genome)
    print("Identified locations of minimum skew: ")
    print(min_skews)

    # Let's take the first minimum skew as ori
    ori = min_skews[0]

    # Find the most frequent 9-mers in the region suggested by ori
    freq_9mers = freq_mismatch_reverse_compliments(genome[ori - 250 : ori + 250], 9, 1)

    return freq_9mers

if __name__ == "__main__":
    with open("Resources/W2/salmonella.txt") as file:
        data = file.read()
    
    clean_data = data.replace("\n", "")
    genome = clean_data.strip()
    
    for i in range(len(genome) - 1):
        if genome[i:i+2] == "/n":
            print(True)

    dnaa_box = find_dnaa_box(genome)

    print(dnaa_box)

    # I get CCGGAAGCT and AGCTTCCGG, which are reverse compliments!