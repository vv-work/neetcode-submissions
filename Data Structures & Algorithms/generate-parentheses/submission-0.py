class Solution: 
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(stack, open, close):     
            nonlocal res 

            if close==n:
                res.append("".join(stack))
                return

            if open<n:
                stack.append("(")
                backtrack(stack,open+1,close)
                stack.pop()

            if close<open:
                stack.append(")")
                backtrack(stack,open,close+1)
                stack.pop()  
        
        backtrack([],0,0) 
        return res
        