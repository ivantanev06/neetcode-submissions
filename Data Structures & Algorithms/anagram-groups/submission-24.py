class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for string in strs:
            counts = [0] * 26

            for char in string:
                index = ord(char) - ord("a")
                counts[index] += 1

            key = tuple(counts)
            if key in groups.keys():
               groups[key].append(string)
            else:
              groups[key] = [string]

        return list(groups.values())
