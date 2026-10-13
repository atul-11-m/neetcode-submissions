class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sAlph = [0] * 26
        tAlph = [0] * 26

        for c in s:
            n = ord(c) - ord("a")
            sAlph[n] = sAlph[n] + 1

        for c in t:
            n = ord(c) - ord("a")
            tAlph[n] = tAlph[n] + 1
        
        if sAlph == tAlph:
            return True
        return False