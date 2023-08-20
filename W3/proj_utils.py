# Yes this is lazy copying code for each week

def hamming_distance(p: str, q: str) -> int:
    dist = 0
    for i, p_i in enumerate(p):
        if p_i != q[i]:
            dist += 1

    return dist

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

def convert_list_to_string_output(list_output: list) -> str:
    return " ".join([str(num) for num in list_output]).strip()

def reverse_compliment(pattern: str):
    compliments = {
        'A': 'T',
        'G': 'C',
        'T': 'A',
        'C':'G'
    }

    compliment = ''
    
    for nuc in pattern:
        compliment += compliments[nuc]

    return compliment[::-1]