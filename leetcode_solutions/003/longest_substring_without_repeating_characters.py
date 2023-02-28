# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        hashmap = {}
        length = 0
        result = 0
        for idx in range(len(s)):
            if s[idx] not in hashmap:
                result = max(result, idx - length + 1)
            else:
                if hashmap[s[idx]] < length:
                    result = max(result, idx - length + 1)
                else:
                    length = hashmap[s[idx]] + 1
            hashmap[s[idx]] = idx
        return result
