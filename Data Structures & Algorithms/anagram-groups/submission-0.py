class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dict = defaultdict(list)

        for word in strs:
            sorted_version = "".join(sorted(word))
            dict[sorted_version].append(word)


        return list(dict.values())     