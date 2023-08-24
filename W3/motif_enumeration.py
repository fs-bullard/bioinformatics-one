from proj_utils import *

def motif_enumeration_bf(dna: list, k: int, d: int) -> set:
    """
    Given a collection of strings dna and an integer d, 
    a k-mer is a (k,d)-motif if it appears in every
    string from dna with at most d mismatches

    Uses brute force to explore all possible solution
    candidates and return a list of the (k,d)-motifs in dna.
    Note: this is not meant to be an optimal solution
    """
    patterns = set()
    n = len(dna[0])
    
    # Look through each of the k-mers in the first dna string
    for a in range(n-k+1):
        pattern = dna[0][a:a+k]
        # Generate the d-neighbourhood of pattern 
        neighbourhood = generate_neighbourhood(pattern, d)
        
        for neighbour in neighbourhood:
            motif = True
            i = 1

            while motif and i < len(dna):
                dna_string = dna[i]

                for j in range(len(dna_string) - k + 1):
                    k_mer = dna_string[j:j+k]

                    if hamming_distance(neighbour, k_mer) <= d:
                        motif = True
                        break

                    motif = False

                i += 1       
                     
            if motif:
                patterns.add(neighbour)

    return patterns

if __name__ == "__main__":
    dna = [
        "TCTATGGGCTCGAAGCATTTCTGAC",
        "CAGGTATATAAGGTCAATGTGGCCT", 
        "TATGCTTACCTACGATAACATATTT", 
        "AATTTCATCTACCTTTATCCAATCT",
        "CACTTTGTCCGATGTGCCTCACCGA",
        "AGTGCGATATCGCTCCTCGCATTGG"]
    k = 5
    d = 2

    patterns = motif_enumeration_bf(dna, k, d)

    print(convert_list_to_string_output(patterns))
    # import numpy as np
    # probs = np.zeros((12))
    # probs[0] = 0.3
    # probs[1] = 0.4
    # probs[2] = 1
    # probs[3] = 1
    # probs[4] = 0.1
    # probs[5] = 0.1
    # probs[6] = 0.1
    # probs[7] = 0.5
    # probs[8] = 0.2
    # probs[9] = 0.3
    # probs[10] = 0.6
    # probs[11] = 0.4
    # entropy = -sum(probs*np.log2(probs))
    # entropy = np.zeros((12))

    # entropy[0] = 0.2*np.log2(0.2) + 0.1*np.log2(0.1) + 0.7*np.log2(0.7)
    # entropy[1] = 0.4*np.log2(0.2) + 0.6*np.log2(0.6)
    # entropy[2] = 0
    # entropy[3] = 0
    # entropy[4] = 0.1*np.log2(0.1) + 0.9*np.log2(0.9)
    # entropy[5] = 0.1*np.log2(0.1) + 0.9*np.log2(0.9)
    # entropy[6] = 0.1*np.log2(0.1) + 0.9*np.log2(0.9)
    # entropy[7] = 0.4*np.log2(0.4) + 0.1*np.log2(0.1) + 0.5*np.log2(0.5)
    # entropy[8] = 0.2*np.log2(0.1) + 0.8*np.log2(0.8)
    # entropy[9] = 0.2*np.log2(0.2) + 0.1*np.log2(0.1) + 0.7*np.log2(0.7)
    # entropy[10] = 0.6*np.log2(0.3) + 0.4*np.log2(0.4)
    # entropy[11] = 0.4*np.log2(0.4) + 0.6*np.log2(0.6)

    # print(sum(entropy))


