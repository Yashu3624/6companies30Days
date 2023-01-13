class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        start = 1 
        end = n -1
        while(end>0):
            if s[0:end] == s[start:n]:
                break
            end -= 1
            start+=1

        return s[0:end]
    
class Solution:
    def longestPrefix(self, s: str) -> str:
        for i in range(len(s)):
            if s[i:]==s[:-i]:
                return s[i:]
        return ''
    