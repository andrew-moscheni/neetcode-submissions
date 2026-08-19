class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums: return []
        if len(nums) < 2: 
            return [] if nums[0] != target else [0]
        
        mem = {}
        for i in range(len(nums)): # O(N)
            if nums[i] in mem.keys():
                return [mem[nums[i]], i]
            else:
                mem[target-nums[i]]=i
        
        return []
        