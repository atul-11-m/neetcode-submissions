class Solution:
    def isValid(self, s: str) -> bool:
        valid = []
        pairs = {'}' : '{', ')' : '(', ']' : '['}
        for c in s:
            if c in pairs:
                if valid and valid[-1] == pairs[c]:
                    valid.pop()
                else:
                    return False
            else:
                valid.append(c)
        if valid:
            return False
        return True
            