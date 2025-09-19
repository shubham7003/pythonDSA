class Solution:
    def genrateParan(self, n: int):
        ans = []

        def backtrack(s, op, cl):
            if len(s) == 2*n:
                ans.append(s)
                return

            if op<n :
                backtrack(s+"(",op+1,cl)
            if op>cl:
                backtrack(s+")",op,cl+1)                
    
        backtrack("",0,0)
        return ans

sol = Solution()
print(sol.genrateParan(3))
