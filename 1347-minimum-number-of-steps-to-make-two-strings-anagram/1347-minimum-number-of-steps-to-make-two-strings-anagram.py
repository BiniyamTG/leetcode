class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_amount = Counter(s)
        t_amount = Counter(t)

        answer = 0

        for i in t_amount.keys():
            if (t_amount[i] - s_amount[i]) > 0:
                answer += (t_amount[i] - s_amount[i])

        return answer
                