class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def get_next(num):
            total = 0
            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total

        seen = set()

        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = get_next(n)

        return True