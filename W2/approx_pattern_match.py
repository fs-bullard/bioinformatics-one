from proj_utils import convert_list_to_string_output
from hamming_distance import hamming_distance

def approximate_pattern_match(pattern: str, text: str, d:int) -> list:
    output = []
    k = len(pattern)
    n = len(text)

    for i in range(n - k + 1):
        possible_pattern = text[i:i+k]

        if hamming_distance(possible_pattern, pattern) <= d:
            output.append(i)
    
    return output

def count_d(pattern: str, text: str, d: int) -> int:
    return len(approximate_pattern_match(pattern, text, d))

def test_apm() -> bool:
    pattern_test = "ATTCTGGA"
    text_test = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT"
    d_test = 3
    expected_out = "6 7 26 27"

    out = convert_list_to_string_output(approximate_pattern_match(pattern_test, text_test, d_test)) 

    if out == expected_out: 
        print("Test Passed")
    else: 
        print("Test Failed")

    return out == expected_out

if __name__ == "__main__":
    test_apm()

    # Test on debugging data
    # for i in range(1, 9):
    #     with open(f"Resources/W2/ApproximatePatternMatching/inputs/input_{i}.txt") as file:
    #         data = file.readlines()
    #     with open(f"Resources/W2/ApproximatePatternMatching/outputs/output_{i}.txt") as file:
    #         data_output = file.read()

    #     pattern = data[0].strip()
    #     text = data[1].strip()
    #     d = int(data[2].strip())

    #     output = data_output.strip()
    #     result = convert_list_to_string_output(approximate_pattern_match(pattern, text, d))
    #     if result == output:
    #         print(f"Test {i} Passed")
    #     else:
    #         print(f"Test {i} Failed")

    # Solve:
    # with open(f"Resources/W2/data_3.txt") as file:
    #     data = file.readlines()
    
    # pattern = data[0].strip()
    # text = data[1].strip()
    # d = int(data[2].strip())

    # result = convert_list_to_string_output(approximate_pattern_match(pattern, text, d))

    # print(result)

    # Count_d

    print(count_d("AAAAA", "AACAAGCTGATAAACATTTAAAGAG", 2))

    with open(f"Resources/W2/data_4.txt") as file:
        data = file.readlines()
    
    pattern = data[0].strip()
    text = data[1].strip()
    d = int(data[2].strip())

    print(count_d(pattern, text, d))




    