from hamming_distance import hamming_distance
from proj_utils import convert_list_to_string_output

def generate_neighbourhood(pattern: str, d: int) -> list[str]:
    n = len(pattern)
    nucleotides = ["A", "C", "G", "T"]

    if d == 0:
        return pattern
    if n == 1:
        return nucleotides

    neighbourhood = []
    suffix_pattern = pattern[1:]
    suffix_neighbours = generate_neighbourhood(suffix_pattern, d)

    for neighbour in suffix_neighbours:
        if hamming_distance(neighbour, suffix_pattern) < d:
            for x in nucleotides:
                neighbourhood.append(x + neighbour)
        else:
            neighbourhood.append(pattern[0] + neighbour)
    
    return neighbourhood

if __name__ == "__main__":
    # Debug dataset
    # for i in range(1, 6):
    #     print("-"*20)
    #     with open(f"Resources/W2/Neighborhood/inputs/input_{i}.txt") as file:
    #         data = file.readlines()
    #     with open(f"Resources/W2/Neighborhood/outputs/output_{i}.txt") as file:
    #         data_output = file.read()

    #     pattern = data[0].strip()
    #     d = int(data[1].strip())        

    #     output = data_output.strip().split('')
    #     result = generate_neighbourhood(pattern, d)

        
    #     if sorted(result) == sorted(output):
    #         print(f"Test {i} Passed")
    #     else:
    #         print(f"Test {i} Failed")
            
    #     print(f"Result: {result}")
    #     print(f"Expected result: {output}")

    # Random dataset

    with open("Resources/W2/data_8.txt") as file:
        data = file.readlines()
    
    pattern = data[0].strip()
    d = int(data[1].strip())

    output = generate_neighbourhood(pattern, d)

    print(convert_list_to_string_output(output))

    """
    Pattern: ACGT
    Neighbourhood:
    d = 0:
    ACGT
    1

    d = 1:
    CCGT
    GCGT
    TCGT
    ...
    3^0*4 = 12

    d = 2:
    3^2*12 = 108

    d = 3
    3^3*4 = 108

    so there are 228 4-mers in the 3-negihborhood of ACGT
    """
    nbh = generate_neighbourhood("ACGT", 3)

    for i, el in enumerate(nbh):
        if el in nbh[:i] + nbh[i+1:]:
            print(True)
    print(len(generate_neighbourhood("ACGT", 3)))
    

