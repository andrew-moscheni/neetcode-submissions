class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs: return []

        from collections import Counter
        res=defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-97]+=1
            res[tuple(count)].append(s)
        return list(res.values())

