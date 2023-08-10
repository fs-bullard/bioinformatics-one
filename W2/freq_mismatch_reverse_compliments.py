from proj_utils import convert_list_to_string_output, reverse_compliment
from neighborhood import generate_neighbourhood

def freq_mismatch_reverse_compliments(text: str, k: int, d: int) -> list:
    """
    Returns the most frequent k-mers in text,
    allowing for mismatches up to d away
    and reverse compliments 
    """
    freq_map = {}
    n = len(text)

    for i in range(n - k + 1):
        substring = text[i:i + k]
        neighbourhood = generate_neighbourhood(substring, d)
        for neighbour in neighbourhood:
            freq_map[neighbour] = freq_map.get(neighbour, 0) + 1
            reverse_neighbour = reverse_compliment(neighbour)
            freq_map[reverse_neighbour] = freq_map.get(reverse_neighbour, 0) + 1

    m = max(freq_map.values())

    patterns = [pattern for pattern, freq in freq_map.items() if freq == m]

    return patterns

if __name__ == "__main__":
    text = "CCGCCGGGGCCGGGGCCAAATACCCGCCCCGGGGCCTACCCCCGCCCCAAACCTACCCGGGGGGAAATACAAAAAATACTACTACGGGAAACCGGGGGGGCCCCAAAGGGCCCCTACAAAGGGAAAGGGCCCCGCCGGGGGGGCCCCGAAAGGGCCCCGGGTACTACCCAAATACCCTACCCGGGGTACCCGCCCCTACAAATACTACCCCCAAAAAACCGCCGGGGGGG"
    k = 5
    d = 3

    print(freq_mismatch_reverse_compliments(text, k, d))
    
