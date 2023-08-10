from proj_utils import convert_list_to_string_output
from approx_pattern_match import count_d
from neighborhood import generate_neighbourhood

def freq_words_with_mismatch(text: str, k: int, d: int) -> list:
    freq_map = {}
    n = len(text)

    for i in range(n - k + 1):
        substring = text[i:i + k]
        neighbourhood = generate_neighbourhood(substring, d)
        for neighbour in neighbourhood:
            freq_map[neighbour] = freq_map.get(neighbour, 0) + 1

    m = max(freq_map.values())

    patterns = [pattern for pattern, freq in freq_map.items() if freq == m]

    return patterns

if __name__ == "__main__":
    # Test on debugging data
    # for i in range(1, 6):
    #     print("-"*20)
    #     with open(f"Resources/W2/FrequentWordsMismatches/inputs/input_{i}.txt") as file:
    #         data = file.readlines()
    #     with open(f"Resources/W2/FrequentWordsMismatches/outputs/output_{i}.txt") as file:
    #         data_output = file.read()

    #     text = data[0].strip()
    #     k = int(data[1].strip().split(' ')[0])
    #     d = int(data[1].strip().split(' ')[1])        

    #     output = data_output.strip().split(" ")
    #     result = freq_words_with_mismatch(text, k, d)
        
    #     if sorted(result) == sorted(output):
    #         print(f"Test {i} Passed")
    #     else:
    #         print(f"Test {i} Failed")
            
    #     print(f"Result: {result}")
    #     print(f"Expected result: {output}")
    text = "GACCAAGGACCCAGCCAGGCACCAGAGTAAGTAAGTAGCAGACGCAAGTAAGTAGCACAAGGCACAAGCAAGGCACCAGAGTAGCAGCAGCACCAGGCACCAGCCAGGACGCACCAGCCAGCCAGAGTAGACCCAGAGTAAGTAAGTAGCAGACAGTAGACCCAGGCAGCAAGTAGCAGCACAAGCAAGCAAGCCAGGACAGTACCAGAGTACAAGCAAGGACCAAGGCAGACAGTAAGTACAAGGACGCAAGTAGACCCAGCCAGGACAGTAAGTAGACCCAGCCAGAGTAGACGCACCAGGCAGACCCAGCAAGCCAGGACAGTAGACCCAGGCACCAGCAAGCAAGAGTAAGTACAAGCCAGGACGCACAAGGACGACGAC"
    k = 5
    d = 3

    print(convert_list_to_string_output(freq_words_with_mismatch(text, k, d)))