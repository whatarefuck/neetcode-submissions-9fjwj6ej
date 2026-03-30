from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramic_dicts = defaultdict(list)
        for str in strs:
            symbol_stats = defaultdict(int)
            for symbol in str:
                symbol_stats[symbol] += 1
            key = tuple(sorted(symbol_stats.items()))
            anagramic_dicts[key].append(str)
        return list(anagramic_dicts.values())

