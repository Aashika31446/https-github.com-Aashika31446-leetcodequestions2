class Solution:
    def reverseDegree(self, s: str) -> int:
        null=0
        sum=0
        for i in range(len(s)):
            x=123-ord(s[i])
            null=x*(i+1)
            sum=sum+null
        return sum
        