def removeDuplicates():
       stack=[0]
       res=""
       for i in S:
           if i== stack[-1]:
               stack.pop()
           else:
               stack.append(i)
       return res.join(stack[1:])
