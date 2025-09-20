class Solution:
    def fun(self, arr):
        max_reach = 0
        for i in range(len(arr)):
            if max_reach < i:
                return False
            max_reach = max(max_reach, arr[i] + i)
            if max_reach > len(arr) - 1:
                return True
        return True

s1 = Solution()
arr = [4,6,-9,87,46,79]
print(s1.fun(arr))