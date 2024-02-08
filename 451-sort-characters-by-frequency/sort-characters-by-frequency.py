class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        sorted_freq = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)

        res = ''
        for k in sorted_freq:
            res += k*freq[k]
        return res
