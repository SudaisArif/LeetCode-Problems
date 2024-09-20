class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2 ** 31 and divisor == -1:
            return 2 ** 31 - 1
        negative = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        count = 0
        while dividend >= divisor:
            tempdivisor = divisor
            mult = 1
            while dividend >= (tempdivisor << 1):
                tempdivisor <<= 1
                mult <<= 1
            dividend -= tempdivisor
            count += mult
        
        if negative:
            return -count
        else:
            return count   
        
        