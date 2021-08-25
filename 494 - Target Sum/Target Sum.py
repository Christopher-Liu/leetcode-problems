class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        self.memo = {}
        index = 0
        relativeSum = 0
        
        return self.findTargetSumWaysRecursive(nums, target, relativeSum, index)
    
    
    def findTargetSumWaysRecurse(self, nums: List[int], target: int, relativeSum: int, index: int):
        
        if (relativeSum, index) in self.memo:
            return self.memo[(relativeSum, index)]

        if index == len(nums) and target == relativeSum:
            return 1
        if index == len(nums) and target != relativeSum:
            return 0
        
        positive = self.findTargetSumWaysRecurse(nums, target, relativeSum + nums[index], index + 1)
        negative = self.findTargetSumWaysRecurse(nums, target, relativeSum - nums[index], index + 1)
        
        self.memo[(relativeSum, index)] = positive + negative
        
        return self.memo[(relativeSum, index)]