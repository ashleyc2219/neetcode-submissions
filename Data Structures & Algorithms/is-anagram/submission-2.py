class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # for string 1 into hashmap
        # for string 2 into hashmap
        # compare 2 hashmap

        stringS = defaultdict(int)
        for c in s:
            stringS[c] += 1
        
        stringT = defaultdict(int)
        for c in t:
            stringT[c] += 1

        return stringS == stringT
        
            
        