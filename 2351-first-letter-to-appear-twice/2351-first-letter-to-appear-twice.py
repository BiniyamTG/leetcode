class Solution:
    def repeatedCharacter(self, s: str) -> str:
        result=[]
        for i in s:
            if i not in result:
                result.append(i)
            else:
                return i
        