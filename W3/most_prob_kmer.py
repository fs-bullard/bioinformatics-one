from median_string import generate_kmers

def most_prob_kmer(text: str, k: int, profile: list[list[float]]) -> str:
    kmer = text[:k]
    result = (calcualte_kmer_prob(kmer, profile), kmer)

    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        kmer_prob = calcualte_kmer_prob(kmer, profile)
        if kmer_prob > result[0]:
            result = (kmer_prob, kmer)
    
    return result[1]

def calcualte_kmer_prob(kmer, profile: list[list[float]]) -> float:
    prob = 1

    nucleotides = { "A" : 0, "C" : 1, "G" : 2, "T" : 3}

    for i, char in enumerate(kmer):
        prob *= profile[nucleotides[char]][i]

    return prob

if __name__ == "__main__":
    # Sample input:

    sample_text = "ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT"
    sample_k = 5
    sample_profile = [
        [0.2, 0.2, 0.3, 0.2, 0.3],
        [0.4, 0.3, 0.1, 0.5, 0.1],
        [0.3, 0.3, 0.5, 0.2, 0.4],
        [0.1, 0.2, 0.1, 0.1, 0.2]
        ]
    
    print("Running test case: ")

    sample_output = most_prob_kmer(sample_text, sample_k, sample_profile)

    print(sample_output)

    # Returns CCGAG as expected

    # Coding challence case:

    with open("Resources/W3/data_5.txt") as file:
        data = file.readlines()

    text= data[0].strip()
    k = int(data[1].strip())
    profile = []
    for i, line in enumerate(data[2:]):
        profile.append([])
        for el in line.split():
            profile[i].append(float(el.strip()))

    output = most_prob_kmer(text, k, profile)

    print(output)