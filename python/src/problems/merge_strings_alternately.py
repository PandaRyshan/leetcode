"""
https://leetcode.cn/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75

LeetCode 1768. 交替合并字符串
给你两个字符串 word1 和 word2 ，请你交替合并字符串，返回合并后的字符串。
注意：交替合并字符串 时，word1 和 word2 的长度可能不相等。
最后一个字符串的长度为 max(word1.length, word2.length) - min(word1.length, word2.length)。
如果 word1.length > word2.length ，那么 word1 的最后一个字符串为 word1 的最后一个字符。
如果 word1.length < word2.length ，那么 word2 的最后一个字符串为 word2 的最后一个字符。
如果两个字符串的长度相等，那么最后一个字符串为 word1 和 word2 的最后一个字符。
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        len1, len2 = len(word1), len(word2)
        max_len = max(len1, len2)
        for i in range(max_len):
            result.append(word1[i] if i < len1 else "")
            result.append(word2[i] if i < len2 else "")
        return "".join(result)


if __name__ == "__main__":
    word1 = "abc"
    word2 = "pqr"
    print(Solution().mergeAlternately(word1, word2))  # "apbqcr"
    word1 = "ab"
    word2 = "pqrs"
    print(Solution().mergeAlternately(word1, word2))  # "apbqrs"
    word1 = "abcd"
    word2 = "pq"
    print(Solution().mergeAlternately(word1, word2))  # "apbqcd"
