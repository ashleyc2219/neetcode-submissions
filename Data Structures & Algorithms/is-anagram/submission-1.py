class Solution:

# (1)
# check length equals
# make string s into hashmap s
# make string t into hashmap t
# compare two dictionary

# (2)
# check length equals
# make string s into hashmap s
# use string t and hashmap s to compare 


    def isAnagram(self, s: str, t: str) -> bool:
        slength = len(s)
        tlength = len(t)
        if (slength != tlength):
            return False;
        

        stable = {}
        for char in s:
            if char in stable:
                stable[char] += 1
            else:
                stable[char] = 1
        
        
        for char in t:
            if char in stable:
                if stable[char] == 1:
                    stable.pop(char)
                else:
                    stable[char] -= 1
            else:
                return False;

        if len(stable) != 0:
            return False
        else:
            return True
        

        