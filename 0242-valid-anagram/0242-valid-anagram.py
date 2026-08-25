class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if len(s) != len(t) :
            return False
        
        hashmap1 = {}
        hashmap2 = {}

        for ch in t:
            hashmap1[ch] = hashmap1.get(ch,0) + 1
        
        for ch2 in s:
            hashmap2[ch2] = hashmap2.get(ch2,0) + 1
        
        if hashmap1 == hashmap2:
            return True
        else:
            return False
        