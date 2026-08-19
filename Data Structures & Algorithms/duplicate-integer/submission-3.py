class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums: return False

        from collections import Counter
        count = Counter(nums)

        return max(count.values()) > 1