class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strings = defaultdict(list)
        for string in strs:
            stringAlph = [0] * 26

            for c in string:
                stringAlph[ord(c) - ord('a')] += 1
            strings[tuple(stringAlph)].append(string)

        return list(strings.values())
            