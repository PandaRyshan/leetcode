from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        hashtable = defaultdict(list)
        for s in strs:
            sorted_str = "".join(sorted(s))
            hashtable[sorted_str].append(s)
        return list(hashtable.values())
