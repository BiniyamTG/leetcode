class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        s=s.split(" ")
        k=len(s[-1])
        return k