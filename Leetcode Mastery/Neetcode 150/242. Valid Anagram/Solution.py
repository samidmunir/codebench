"""
    Runtime: 16ms
    Memory: 17.80MB
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}

        if len(t) != len(s):
            return False

        for letter in s:
            if letter not in sMap:
                sMap[letter] = 1
            else:
                sMap[letter] += 1

        for letter in t:
            if letter not in tMap:
                tMap[letter] = 1
            else:
                tMap[letter] += 1

        for letter in t:
            if letter in sMap and tMap[letter] == sMap[letter]:
                continue
            else:
                return False
            
        return True