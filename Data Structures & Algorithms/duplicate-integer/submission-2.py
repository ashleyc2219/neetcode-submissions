class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        m = dict()
        for n in nums:
            if n in m:
                return True
            else:
                m[n] = 1
        return False
        
            