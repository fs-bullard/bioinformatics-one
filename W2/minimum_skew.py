from calculate_skew import calculate_skew
import matplotlib.pyplot as plt
from proj_utils import convert_list_to_string_output

def minimum_skew(genome: str) -> str:
    """
    Returns the positions of minimum skew in genome
    """
    skews = calculate_skew(genome)
    min_skew = min(skews)

    # plt.plot(skews)
    # plt.show()

    output = [i for i, skew in enumerate(skews) if skew == min_skew]
    
    return output

def test_minimum_skew() -> bool:
    test_genome = "TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"
    test_output = "11 24"
    
    test_min_skew = convert_list_to_string_output(minimum_skew(test_genome))

    if test_min_skew == test_output: print("Test Passed")

    return test_min_skew == test_output

if __name__ == "__main__":
    test_minimum_skew()

    with open("Resources/W2/data_1.txt") as file:
        genome = file.read().strip()

    minimum_skew_points = convert_list_to_string_output(minimum_skew(genome))

    print(minimum_skew_points)

    print(minimum_skew("CATTCCAGTACTTCGATGATGGCGTGAAGA"))