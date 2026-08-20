class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        if k < 1: return []

        counter = Counter(nums)
        lst = sorted(counter.items(), key=lambda x: x[1], reverse=True)[:k]
        return [x[0] for x in lst]
        