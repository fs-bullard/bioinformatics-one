from freq_words import generate_freq_map

def find_clumps(genome: str, k: int, L: int, t: int):
    patterns = set()
        
    for i in range(len(genome) - L + 1):     
        freq_map = generate_freq_map(genome[i:i + L], k)
        
        for key in freq_map.keys():
            if freq_map[key] >= t:
                patterns.add(key)

    # clumps = ' '.join(patterns)

    return len(patterns)

def get_clumps(genome, k, L, t):
    kmers = KmerSequence(L-k, t)

    for kmer in sliding_window(genome, k):
        kmers.add(kmer)

    return kmers.clumps

class KmerSequence(object):
    __slots__ = ['order', 'counts', 'limit', 'clumps', 't']

    def __init__(self, limit, threshold):
        self.order = deque()
        self.counts = Counter()
        self.limit = limit
        self.clumps = set()
        self.t = threshold

    def add(self, kmer):
        if len(self.order) > self.limit:
            self._remove_oldest()
        self._add_one(kmer)

    def _add_one(self,kmer):
        self.order.append(kmer)
        new_count = self.counts[kmer] + 1
        self.counts[kmer] = new_count

        if new_count == self.t:
            self.clumps.add(kmer)

    def _remove_oldest(self):
        self.counts[self.order.popleft()] -= 1

if __name__ == '__main__':
    with open('Resources/W1/data_7.txt') as file:
        data = file.read()

    genome = data.strip()
    
    # integers = data[1].strip()
    # genome = 'CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA'
    integers = '9 500 3'
    
    k, L, t = map(int, integers.split())    
    
    clumps = find_clumps(genome, k, L, t)

    print(clumps)
    print(f'k: {k}, L: {L}, t: {t}')