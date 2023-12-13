class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = ""
        max_len = 0

        for c in s:
            if c not in substr:
                substr += c
                if len(substr) > max_len:
                    max_len = len(substr)
            else:
                substr = substr[substr.index(c) + 1:] + c

        return max_len

    def lengthOfLongestSubstring_hash(self, s: str) -> int:
        prev, res, c_dict = -1, 0, {}

        for i, c in enumerate(s):
            if c in c_dict and c_dict[c] > prev:
                prev = c_dict[c]
                c_dict[c] = i
            else:
                c_dict[c] = i
                res = max(res, i - prev)

        return res
