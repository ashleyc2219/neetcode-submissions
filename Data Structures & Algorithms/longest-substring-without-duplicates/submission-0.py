class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        i = 0          
        result = 0

        for j in range(len(s)):          
            while s[j] in substring:
                substring.remove(s[i])
                i += 1

            substring.add(s[j])
            result = max(result, j - i + 1)

        return result