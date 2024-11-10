class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # Convert the list of digits into a string
        num_str = ''.join(map(str, digits))

        # Convert the string to an integer
        num = int(num_str) + 1

        # Convert the integer back to a list of digits
        result = [int(d) for d in str(num)]

        return result 


        
    
        