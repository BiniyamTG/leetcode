class Solution:
    def isValid(self, s: str) -> bool:
            brackets = {')':'(', ']':'[', '}':'{'}
            operation  = []
            for c in s:
                if not operation or c not in brackets:
                    operation.append(c)
                else:
                    if operation[-1] != brackets[c]:
                        return False
                    else:
                        operation.pop()
            return operation == []


            