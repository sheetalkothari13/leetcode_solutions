class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort()
        first = strs[0] 
        second = strs[-1]
        i = 0
        while i < len(first) and i < len(second) and first[i] == second[i]:
            i += 1
        return first[:i]
        