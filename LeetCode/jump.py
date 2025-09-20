class Solution:
    def fun(self,arr):
        range = 0
        for i in range(len(arr)):
            if(range < i): return False
            range = max(range, arr[i]+i)
            if(range > len(arr)-1): return True
        return True

s1 = Solution()
arr = [4,6,-9,87,46,79]
print(s1.fun(arr))