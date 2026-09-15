class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        n = 26

        for s in strs:
            alphebetList = [0] * n
            for character in s:
                characterIndex = ord(character) - ord('a')
                alphebetList[characterIndex] += 1
            hashmap[tuple(alphebetList)].append(s)
        
        return list(hashmap.values())


        