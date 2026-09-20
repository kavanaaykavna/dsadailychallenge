class Solution:
    def reverseDegree(self, s: str) -> int:
        a = len(s)
        
        degree = 0 
        for i in range(1, a+1):
            value = ord(s[i-1]) - ord('a') + 1
            j = 27 - value
            p = i*j 
            degree = degree + p 
        return degree
obj = Solution()
res = obj.reverseDegree("zaza")
print(res)
