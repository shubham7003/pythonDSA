class Solution:
    def maxSubarray(self,arr):
        start = end = 0
        tempStart = 0
        highScore = arr[0]
        sum = 0
        for i in range(len(arr)):
            sum += arr[i]
            start = tempStart
            end = i
            highScore = max(sum,highScore)
            if (sum<0) : 
                sum = 0
                tempStart = i+1


        return highScore, arr[start:end+1]
    
s1 = Solution()
arr1 = [5,-5,8,7,3,-1,5]
print(s1.maxSubarray(arr1))