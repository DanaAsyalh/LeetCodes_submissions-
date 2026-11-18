class Solution:
    def isPalindrome(self, s: str) -> bool:
        #start with an empty string
        start = ""

        # go throgh every char in list
        for char in s:

        #check char is alphabet
            if char.isalnum():
                start +=char.lower()
        #make lowercase
        
        #return back if start == start[::-1]
        return start == start[::-1]