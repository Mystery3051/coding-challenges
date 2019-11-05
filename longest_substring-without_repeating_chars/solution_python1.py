from collections import deque


class Solution:
        def lengthOfLongestSubstring(self, s: str) -> int:
            if s == "" or s is None:
                return 0

            substring = deque(s[0])
            max_length = curr_length = 1
            for i in range(1, len(s)):
                if s[i] not in substring:
                    substring.append(s[i])
                    curr_length += 1
                else:
                    if max_length < curr_length:
                        max_length = curr_length
                    while substring.popleft() != s[i]:
                        curr_length -= 1
                    substring.append(s[i])

            return max(curr_length, max_length)
