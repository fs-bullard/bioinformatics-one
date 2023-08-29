from most_prob_kmer import most_prob_kmer
from proj_utils import convert_list_to_string_output

def greedy_motif_search(k: int, t:int, dna: list[str]) -> list[str]:
    best_motifs = (t*k, [])

    for i in range(len(dna[0]) - k + 1):
        kmer = dna[0][i:i+k]
        motifs = [kmer]

        for text in dna[1:]:
            profile = generate_profile(motifs)
            motif = most_prob_kmer(text, k, profile)
            motifs.append(motif)
        
        score = generate_score(motifs)

        if score < best_motifs[0]:
            best_motifs = (score, motifs)

    return best_motifs[1]

def generate_profile(motifs: list[str]) -> list[list[float]]:
    nucleotides = { "A" : 0, "C" : 1, "G" : 2, "T" : 3}
    profile = [
        [],
        [],
        [],
        []
    ]
    k = len(motifs[0])
    # print(f"Motifs: {motifs}")

    for i in range(k):
        column = [motifs[j][i] for j in range(len(motifs))]
        for line in profile: line.append(0)

        for nuc in column:
            profile[nucleotides[nuc]][i] += 1 / len(motifs)

    # print(profile)
    return profile

def gms_with_pseudocounts(k: int, t:int, dna: list[str]) -> list[str]:
    best_motifs = (t*k, [])

    for i in range(len(dna[0]) - k + 1):
        kmer = dna[0][i:i+k]
        motifs = [kmer]

        for text in dna[1:]:
            profile = generate_laplace_profile(motifs)
            motif = most_prob_kmer(text, k, profile)
            motifs.append(motif)
        
        score = generate_score(motifs)

        if score < best_motifs[0]:
            best_motifs = (score, motifs)

    return best_motifs[1]

def generate_laplace_profile(motifs: list[str]) -> list[list[float]]:
    nucleotides = { "A" : 0, "C" : 1, "G" : 2, "T" : 3}
    profile = [
        [],
        [],
        [],
        []
    ]
    k = len(motifs[0])
    # print(f"Motifs: {motifs}")

    for i in range(k):
        column = [motifs[j][i] for j in range(len(motifs))]
        for line in profile: line.append(1)

        for nuc in column:
            profile[nucleotides[nuc]][i] += 1 / len(motifs)

    # print(profile)
    return profile

def generate_score(motifs: list[str]) -> int:
    score = 0
    k = len(motifs[0])

    # print(f"Motifs: {motifs}")

    for i in range(k):
        column = [motifs[j][i] for j in range(len(motifs))]
        freqs = { "A" : 0, "C" : 0, "G" : 0, "T" : 0}

        for nuc in column:
            freqs[nuc] += 1
        
        score += sum(sorted(freqs.values())[:-1])

    return score

if __name__ == "__main__":
    sample_k = 3
    sample_t = 5
    sample_dna = [
        "GGCGTTCAGGCA", 
        "AAGAATCAGTCA",
        "CAAGGAGTTCGC",
        "CACGTCAATCAC",
        "CAATAATATTCG"
    ]

    print("-"*10 + "Sample test" + "-"*10)
    
    sample_output = greedy_motif_search(sample_k, sample_t, sample_dna)

    print(convert_list_to_string_output(sample_output))

    print("-"*10 + "Submission" + "-"*10)

    with open("Resources/W3/data_6.txt") as file:
        data = file.readlines()

    k = int(data[0].split()[0])
    t = int(data[0].split()[1])
    dna = data[1].split()

    output = greedy_motif_search(k, t, dna)

    print(convert_list_to_string_output(output))

    print("-"*10 + "Improved search" + "-"*10)

    with open("Resources/W3/data_7.txt") as file:
        data = file.readlines()

    k = int(data[0].split()[0])
    t = int(data[0].split()[1])
    dna = data[1].split()

    output = gms_with_pseudocounts(k, t, dna)

    print(convert_list_to_string_output(output))