class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        elif x==1 or x==2:
            return 1
        for i in range(2,x):
            if i**2 > x:
                return (i-1)
                break

        