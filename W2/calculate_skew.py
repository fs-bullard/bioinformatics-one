from proj_utils import convert_list_to_string_output

def calculate_skew(genome: str) -> str:
    """
    Returns the skew at each index in the genome, where 
    skew[i] is the difference between the number of G and C
    nucleotides in genome[:i]
    """
    skews = [0]
    n = len(genome)
    for i in range(n):
        skew = skews[i]
        if genome[i] == "G":
            skew += 1
        elif genome[i] == "C":
            skew -= 1
        skews.append(skew)
    return skews


def test_skew() -> bool:
    test_genome = "CATGGGCATCGGCCATACGCC"
    test_output = "0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2"

    test_skew = convert_list_to_string_output(calculate_skew(test_genome))
    return test_skew == test_output

if __name__ == '__main__':
    print(test_skew())

    print(convert_list_to_string_output(calculate_skew("GAGCCACCGCGATA")))