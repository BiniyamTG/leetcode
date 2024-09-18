class Solution:
    def calPoints(self, operations: List[str]) -> int:
        new_array=[]
        for i in operations:
            if i=="C":
                new_array.pop()
            elif i=="D":
                new_array.append(new_array[-1]*2)
            elif i=="+":
                new_array.append(new_array[-1]+new_array[-2])
            else:
                new_array.append(int(i))

        return (sum(new_array))
        