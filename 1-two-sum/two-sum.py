class Solution:
    def twoSum(self, num, target):
        seen={}
        for i,n in enumerate(num):
            result=target-n
            if result in seen:
                return [seen[result],i]
            seen[n]=i