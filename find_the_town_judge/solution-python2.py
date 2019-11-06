from typing import List

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        judge_candidate = [True] * N
        trust_factor = [0] * N

        for villager, trustworthy in trust:
            judge_candidate[villager - 1] = False
            trust_factor[trustworthy - 1] += 1

        max_trust = max(trust_factor)

        if max_trust != N - 1:
            return -1

        for i in range(N):
            if judge_candidate[i] and trust_factor[i] == max_trust:
                return i + 1

        return -1
