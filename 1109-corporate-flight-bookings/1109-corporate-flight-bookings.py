class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        result=n*[0]
        for i in bookings:
            start=i[0]-1
            end=i[1]
            sum=i[2]
            result[start]=result[start]+sum
            if end<n:
                result[end]=result[end]-sum
        value=0
        for i in range(n):
            value=value+result[i]
            result[i]=value
        return result
        