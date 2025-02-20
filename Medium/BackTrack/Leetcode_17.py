# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]

def letterCombinations(digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result=[]
        key={
            "2":"abc","3":"def",
            "4":"ghi","5":"jkl",
            "6":"mno","7":"pqrs",
            "8":"tuv","9":"wxyz"
        }
        if not digits:
            return []
        def backtrack(utga,combination):
            if utga==len(digits):
                result.append("".join(combination))
                return
            bolomjit_utga=key[digits[utga]] 
            for useg in bolomjit_utga: 
                combination.append(useg)
                backtrack(utga+1,combination)
                combination.pop()
        backtrack(0,[])
        return result
                
digits="68"
print(letterCombinations(digits))
        

