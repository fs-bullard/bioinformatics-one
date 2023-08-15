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
        "GGCTGAGACTCCTGAGTTGGTACTT",
        "GATGGCGGCAGATGGAGGTTGGGTT", 
        "CTAGCCTTGAGTTGTGCGTACCGAT", 
        "GTTGGAGCGCTACAGAAATTATGCA",
        "TGAGAGATGTGGGAATGGTGAGGCA",
        "GCTGGCGCAATTTCGGTCCAAGATT"]
    k = 5
    d = 2

    patterns = motif_enumeration_bf(dna, k, d)

    print(convert_list_to_string_output(patterns))