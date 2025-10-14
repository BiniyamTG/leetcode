class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = int(''.join(map(str, digits)))
        updated=number+1
        name = [int(d) for d in str(updated)]
        return name

        