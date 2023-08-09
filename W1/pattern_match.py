def pattern_match(pattern: str, genome: str):
    positions = ''

    k = len(pattern)

    for i in range(len(genome) - k + 1):
        if genome[i: i + k] == pattern:
            positions += str(i) + ' '
    
    return positions.strip()

if __name__ == '__main__':
    with open('Resources/W1/Vibrio_cholerae.txt') as file:
        data = file.readlines()

    # pattern = data[0].strip()
    genome = data[0].strip()
    pattern = 'CTTGATCAT'

    positions = pattern_match(pattern, genome)

    print(positions)