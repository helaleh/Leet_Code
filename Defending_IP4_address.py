def defangIPaddr(address):
       res=""
       b=[]
       for i in list(address):
           if i ==".":
               b.append("[.]")
           else:
               b.append(i)
       return res.join(b)
