class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for index in range(len(nums)):
            rem = target - nums[index]
            if rem in seen:
                return ([seen[rem], index])
            seen[nums[index]] = index