from typing import List

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

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        
        if len(strs) == 1:
            currentList = []
            currentList.append(strs[0])
            result.append(currentList)
            return result
        
        visited = {}

        i = 0
        while i < len(strs):
            if i in visited:
                i += 1
            else:
                currentList = []
                currentWord = strs[i]
                visited[i] = True
                currentList.append(currentWord)
                k = i + 1
                while k < len(strs):
                    testWord = strs[k]
                    if k not in visited and self.isAnagram(s = currentWord, t = testWord):
                        visited[k] = True
                        currentList.append(testWord)
                    k += 1
                result.append(currentList)
                i += 1
        
        return result