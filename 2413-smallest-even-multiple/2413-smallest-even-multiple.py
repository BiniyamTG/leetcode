class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        #if it is smallest even multiple of 2 and n it is the same as smallest multiple of 2 and n
        counter=n
        while(True): #to itterate the infinite loop
            if counter%2==counter%n:
                 #check if the counter is multiple of 2 and n 
                 return counter
            counter=counter+1

        
