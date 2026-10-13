class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        charArr1 = [0] * 26
        charArr2 = [0] * 26

        for c in s:
            charArr1[ord(c) - ord("a")] += 1
        for c in t:
            charArr2[ord(c) - ord("a")] += 1
        return charArr1 == charArr2