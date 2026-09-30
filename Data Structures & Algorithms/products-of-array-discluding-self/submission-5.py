class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        preProduct = [0] * n
        postProduct = [0] * n
        result = [0] * n
        preProduct[0] = 1
        postProduct[n-1] = 1
        for i in range(1, n):
            preProduct[i] = preProduct[i-1] * nums[i-1]

        for i in range(len(nums) - 2, -1, -1):
            postProduct[i] = postProduct[i+1] * nums[i+1]
        
        for i in range(len(nums)):
            result[i] = preProduct[i] * postProduct[i]

        return result

        