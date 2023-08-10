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
