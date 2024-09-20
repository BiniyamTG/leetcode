class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        result = []
        
        for i in range(len(temperatures)):
            while result and result[-1][0] < temperatures[i]:
                answer[result[-1][1]] = i - result[-1][1]
                result.pop()
            result.append([temperatures[i], i])
                            
        return answer
        