class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs: return []

        from collections import Counter
        mem = {}
        check = [0]*26
        for i in range(len(strs)):
            counter = Counter(strs[i])
            for char in counter.keys():
                check[ord(char)-97] += counter[char]

            if tuple(check) not in mem.keys():
                mem[tuple(check)] = [strs[i]]
            else:
                mem[tuple(check)].append(strs[i])
            check = [0]*26
        return list(mem.values())

