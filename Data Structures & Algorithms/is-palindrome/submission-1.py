class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanString = ''
        for c in s:
            if c.isalpha() or c.isnumeric():
                cleanString += c.lower()
        return cleanString == cleanString[::-1]
        
            