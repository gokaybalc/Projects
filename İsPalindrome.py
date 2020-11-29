class Solution(object):
    def isPalindrome(self,x):
        self.x=x
        self.x=str(self.x)
        median=len(self.x)%2
        if median==0:
            while len(self.x)!=0:
                if self.x[0]==self.x[-1]:
                    self.x=self.x[1:-1]
                else:
                    return False
            return True
        else:
            while len(self.x)!=1:
                if self.x[0]==self.x[-1]:
                    self.x=self.x[1:-1]
                else:
                    return False
            return True

g=Solution()
print(g.isPolindrome(12))

