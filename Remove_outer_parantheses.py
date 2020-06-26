def removeOuterParentheses(S: str):
       count, result = 0, ''
       for c in S:
           if c == ')': count -= 1
           if count != 0: result += c
           if c == '(': count+=1

       return result
