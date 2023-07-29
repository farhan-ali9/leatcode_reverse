class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        max=2**31
        min=-2**31
        reverse=0
        is_negative = x < 0
        x = abs(x)
        while x!=0:
            remainder = x % 10
            reverse = (reverse * 10) + remainder
            x //= 10
        if is_negative:
            reverse = -reverse
        if reverse >max or reverse < min:
            return 0
        return reverse
