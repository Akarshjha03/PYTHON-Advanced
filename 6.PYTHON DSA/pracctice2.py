def postfix(exp):
  exp=exp.split()
  stack=[]
  
  for i in exp:
    if i not in "/*+-":
      stack.append(int(i))
    
    else:
      r=stack.pop()
      l=stack.pop()
      
      if i=="+":
        stack.append(l+r)
      elif i=="-":
        stack.append(l-r)
      elif i=="*":
        stack.append(l*r)
      elif i=="/":
        stack.append(l/r)
      return stack.pop()
  
e="2 3 5 + *"
print("value of postfix expression is:",postfix(e))
