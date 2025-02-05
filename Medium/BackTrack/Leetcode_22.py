# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
# Input: n = 1
# Output: ["()"]

def generateParenthesis(n):
        """
        :type n: int
        :rtype: List[str]
        """
        result=[]
        parenthesis_container=[]
        def backtrack(open, closed):
            if open==closed==n: #rule:1
                result.append("".join(parenthesis_container))
            if open<n: #rule:2
                parenthesis_container.append("(")
                backtrack(open+1,closed)
                parenthesis_container.pop()
            if open>closed: #rule:3
                parenthesis_container.append(")")
                backtrack(open,closed+1)
                parenthesis_container.pop()
        backtrack(0,0)
        return result
        
n=3
print(generateParenthesis(n))