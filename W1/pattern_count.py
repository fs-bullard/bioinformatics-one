def pattern_count(text, pattern):
    k = len(pattern)
    count = 0

    for i in range(len(text) - k + 1):
        substring = text[i:i + k]
        if substring == pattern:
            count += 1

    return count

if __name__ == '__main__':
    data = open('dataset_30272_6 (1).txt').readlines()
    
    text = data[0].strip()
    pattern = data[1].strip()

    count = pattern_count(text, pattern)

    print(count)