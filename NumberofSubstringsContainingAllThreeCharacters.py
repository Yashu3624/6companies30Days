class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        a,b,c = 0 , 0 , 0 
        res = 0 
        n = len(s)
        index , i = 0 , 0
        while i < n :
            if s[i] == 'a':
                a += 1
            elif s[i] == 'b':
                b += 1
            else:
                c += 1
            while a > 0 and b > 0 and c > 0 :
                res += n-i
                if s[index]=='a':
                    a-=1
                elif s[index]=='b':
                    b-=1
                else:
                    c-=1
                index +=1
            i += 1
        return res        