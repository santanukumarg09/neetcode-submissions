class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        chars = {}
        for char in s:
            if char not in chars:
                chars[char] = 1
            else:
                chars[char] = chars[char] + 1


        for char in t:
            if char not in chars:
                return False            
            chars[char] -= 1
            
            if chars[char] < 0:
                return False
        return True