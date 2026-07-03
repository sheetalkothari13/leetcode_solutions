class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_cnt = Counter(p)
        w_cnt = {}
        l = 0
        ans = []

        for r in range(len(s)):
            w_cnt[s[r]] = w_cnt.get(s[r],0) + 1

            if r-l+1 > len(p):
                w_cnt[s[l]] -= 1
                if w_cnt[s[l]] == 0:
                    del w_cnt[s[l]]
                l += 1
            
            if r-l+1 == len(p):
                if w_cnt == p_cnt:
                    ans.append(l)
        return ans
    
        