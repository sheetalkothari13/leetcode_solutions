from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        chc = Counter(s)
        a = sorted(chc.keys(), key=lambda c: -chc[c])
        result=''
        for c in a:
            result+= c*chc[c]
        return result
