from proj_utils import hamming_distance
nucleotides = ["A", "T", "G", "C"]

def median_string(dna: list[str], k: int) -> str:
    d = len(dna) * len(dna[0])
    kmers = generate_kmers(k)
    medians = []

    for kmer in kmers:
        d_kmer = calculate_distance(kmer, dna)
        if d_kmer <= d:
            d = d_kmer
          
            medians.append((d, kmer))

    return [median[1] for median in medians if median[0] == d]

def calculate_distance(pattern: str, dna: list[str]) -> int:
    k = len(pattern)
    d = 0

    for dna_string in dna:
        ham_dist = k + 1
        for j in range(len(dna_string) - k + 1):
            kmer = dna_string[j:j+k]
            hamming_kmer = hamming_distance(kmer, pattern)

            ham_dist = min(hamming_kmer, ham_dist)
        d += ham_dist

    return d

def generate_kmers(k: int) -> list[str]:
    if k == 0:
        return []
    elif k == 1:
        return nucleotides

    kmers = []
    for nuc in nucleotides:
        sub_kmers = generate_kmers(k - 1)
        for sub_kmer in sub_kmers:
            kmers.append(nuc + sub_kmer)

    return kmers


if __name__ == "__main__":
    # Run calculate distance
    with open("Resources/W3/data_4.txt") as file:
        data = file.readlines()
    

    pattern = data[0].strip()
    dna = data[1].split()
    
    print(calculate_distance(pattern, dna))

    # Run median string
    with open("Resources/W3/data_3.txt") as file:
        data = file.readlines()
    

    k = int(data[0].strip())
    dna = data[1].split()

    print(median_string(dna, k))

