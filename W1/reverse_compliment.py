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

if __name__ == '__main__':
    with open('Resources/W1/data_2.txt') as file:
        pattern = file.readlines()[0].strip()


    output = reverse_compliment('CTTGATCAT') 

    print(output)