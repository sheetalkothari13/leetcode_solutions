class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        sign = 1
        num = 0

        while i<n and s[i]== " ":
            i += 1
        if i<n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
        while i<n and s[i].isdigit():
            digit = int(s[i])
            num = num * 10 + digit 
            i += 1
        num *= sign
        int_min = -2 ** 31
        int_max = (2 ** 31) - 1 
        if num < int_min:
            return int_min
        if num > int_max:
            return int_max
        
        return num
