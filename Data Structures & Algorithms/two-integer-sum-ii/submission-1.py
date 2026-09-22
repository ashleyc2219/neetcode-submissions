class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        for i in range(0, len(numbers)):
            remain = target - (numbers[left] + numbers[right])
            if remain < 0:
                right-=1
            if remain > 0:
                left+=1
            if remain == 0:
                break
        return [left + 1, right + 1]
                    