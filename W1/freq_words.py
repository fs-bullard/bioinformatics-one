def generate_freq_map(text: str, k: int):
    freq_map = {}

    for i in range(len(text) - k + 1):
        k_mer = text[i:i+k]

        if k_mer not in freq_map:
            freq_map[k_mer] = 1
        else:
            freq_map[k_mer] += 1

    return freq_map


def freq_words(text: str, k: int):
    freq_map = generate_freq_map(text, k)

    max_freq = max(freq_map.values())

    freq_patterns = [k_mer for k_mer, freq in freq_map.items() if freq == max_freq]
        
    return freq_patterns


if __name__ == '__main__':
    print('-'*20 + ' RUNNING FREQUENT WORDS CALULATION ' + '-'*20)

    with open('Resources/W1/data_1.txt') as file:
        data = file.readlines()

    text = data[0].strip()
    k = int(data[1].strip())

    freq_patterns = freq_words(text, k)

    for word in freq_patterns:
        print(word)

