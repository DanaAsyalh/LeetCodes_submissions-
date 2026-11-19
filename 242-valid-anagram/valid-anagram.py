class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check if len s and len t are the same
        #make dictionary countS and countT
        # go through every char in len(s) 
        # count char in countT and countS

        countS = {}
        countT = {} 
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1

        return countS == countT    

        