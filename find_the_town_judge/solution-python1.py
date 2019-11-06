class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        judge_candidate = [True] * N
        current_candidate = 0
        trust_factor = {k: 0 for k in range(N)}

        for villager, trustworthy in trust:
            judge_candidate[villager - 1] = False
            trust_factor[trustworthy - 1] += 1

        current_candidate = -1
        for i in range(N):
            if judge_candidate[i] and current_candidate == -1:
                current_candidate = i
                break

        if current_candidate == -1:
            return -1

        max_trust = max(trust_factor.values())

        if max_trust == N - 1 and trust_factor[current_candidate] == max_trust:
            return current_candidate + 1
        else:
            return -1
