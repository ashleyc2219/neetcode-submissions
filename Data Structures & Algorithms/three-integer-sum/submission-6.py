class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            currentTarget = nums[i] * (-1)
            # nums[l] + nums[r] = target
            while r > l:
                if ((nums[l] + nums[r]) > currentTarget):
                    r -= 1
                    continue
                if ((nums[l] + nums[r]) < currentTarget):
                    l += 1
                    continue
                if ((nums[l] + nums[r]) == currentTarget):
                    res = [nums[i], nums[l], nums[r]]
                    if res not in result:
                        result.append(res)
                    l += 1
        return result



        