class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        total = 0
        for i in range(n):
            fr = [0] * 26
            for j in range(i,n):
                char_ind = ord(s[j])-ord('a')
                fr[char_ind] +=1
                maxf=0
                minf=float('inf')
                for f in fr:
                    if f>0:
                        maxf = max(maxf,f)
                        minf = min(minf,f)
                total += (maxf-minf)
        return total