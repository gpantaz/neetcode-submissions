class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
        # anagrams = defaultdict(list)
        # for current_string in strs:
        #     freqs = Counter(current_string)
        #     hash_key = ""
        #     for chara in sorted(list(freqs.keys())):
        #         hash_key += f"{chara}{freqs[chara]}"
        #     anagrams[hash_key].append(current_string)

        # res = []
        # for key, anagrams_strings in anagrams.items():
        #     res.append(anagrams_strings)
        # return res
