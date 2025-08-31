class Solution:
    def reverse(self, x: int) -> int:
        int_min , int_max = -2**31 , 2**31 -1
        if x < 0:
            s = -1
        else:
            s = 1
        abs_x = abs(x)
        rev = int(str(abs_x)[::-1])
        res = s * rev

        if res<int_min or res>int_max :
            return 0
        else:
            return res
        