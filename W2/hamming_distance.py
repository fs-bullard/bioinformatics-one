def hamming_distance(p: str, q: str) -> int:
    dist = 0
    for i, p_i in enumerate(p):
        if p_i != q[i]:
            dist += 1

    return dist

def test_hamming_distance() -> bool:
    p_test = "GGGCCGTTGGT"
    q_test = "GGACCGTTGAC"
    exp_out = 3

    out = hamming_distance(p_test, q_test)

    if out == exp_out: print("Test Passed")

    return out == exp_out

if __name__ == '__main__':
    test_hamming_distance()

    with open("Resources/W2/data_2.txt") as file:
        data = file.readlines()
    
    p = data[0].strip()
    q = data[1].strip()

    print(hamming_distance(p, q))
