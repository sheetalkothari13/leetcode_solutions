class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        used = set()

        for i in range(len(s)):
            ch1 = s[i]
            ch2 = t[i]

            if ch1 in mapping:
                if mapping[ch1] != ch2:
                    return False
            else:
                if ch2 in used:
                    return False
                mapping[ch1] = ch2
                used.add(ch2)

        return True
        
        
        
        