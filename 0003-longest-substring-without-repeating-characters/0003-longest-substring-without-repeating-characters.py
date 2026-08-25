class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow = 0
        max_len = 0
        hashmap = {}

        for fast in range(len(s)):
            if s[fast] in hashmap and hashmap[s[fast]]>=slow :
                slow = hashmap[s[fast]]+1
            hashmap[s[fast]] = fast
            max_len = max(max_len,fast-slow+1)
        
        return max_len

        