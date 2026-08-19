class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s: return False
        if not t: return False

        from collections import Counter
        first = Counter(s) # O(N)
        second = Counter(t) # O(N)

        return first == second
        