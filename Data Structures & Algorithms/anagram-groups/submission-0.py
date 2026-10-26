class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for j in strs:
           d["".join(sorted(j))].append(j)
        return list(d.values())