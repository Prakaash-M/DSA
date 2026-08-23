class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            y = target - n
            if y in seen:
                return([seen[y],i])
            seen[n] = i

            
                