class Solution:
    def isAnagram(self, s:str , t:str) -> bool:
        #check if len s == len t
        #sorted s == sorted t is true
        if len(s) != len(t):
            return False


        return sorted(s) == sorted(t)    















#old
      #check of length of s == length t
      #if true then make list to put char s in 
      #go throgh every char in s to check if every char in s exists in t
      #return answer


