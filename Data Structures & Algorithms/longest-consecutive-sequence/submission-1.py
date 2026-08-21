class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        hashed = set(nums)

        longest=0
        for num in hashed:
            if num-1 in hashed: # not start of sequence
                continue
            length = 1
            while num+length in hashed:
                length+=1
            longest=max(longest,length)
        return longest
        