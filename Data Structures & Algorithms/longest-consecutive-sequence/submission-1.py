class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        result = 0
        for n in numbers:
            length = 0
            if (n - 1) not in numbers:
                length = 1
                while n + length in numbers:
                        length += 1
                result = max(length, result)
        return result



        