class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_window = Counter(s1)
        w_cnt = {}
        l = 0
        for r in range(len(s2)):
            w_cnt[s2[r]] = w_cnt.get(s2[r],0) + 1
            if r-l+1 > len(s1):
                w_cnt[s2[l]] -= 1
                if w_cnt[s2[l]] == 0:
                    del w_cnt[s2[l]]
                l += 1
            if r-l+1 == len(s1):
                if w_cnt == s1_window:
                    return True
        return False
