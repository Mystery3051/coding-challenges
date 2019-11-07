from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[
        int]:

        answer = [0] * n
        for start, end, seats in bookings:
            answer[start - 1] += seats
            if end < n:
                answer[end] -= seats

        for i in range(1, n):
            answer[i] += answer[i - 1]

        return answer
