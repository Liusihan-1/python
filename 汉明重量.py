class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=0
        if n==0:
            return 0
        while n>0:
            n=n&(n-1)
            ans+=1
        return ans
