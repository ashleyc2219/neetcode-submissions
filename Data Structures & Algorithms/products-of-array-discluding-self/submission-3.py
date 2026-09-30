class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preProduct = [0] * len(nums)
        postProduct = [0] * len(nums)
        result = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0 :
                preProduct[i] = 1
            else:
                preProduct[i] = preProduct[i-1] * nums[i-1]

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                postProduct[i] = 1
            else:
                postProduct[i] = postProduct[i+1] * nums[i+1]
        
        for i in range(len(nums)):
            result[i] = preProduct[i] * postProduct[i]

        return result

        