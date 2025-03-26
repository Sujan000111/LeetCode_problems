def RoomanToInterger(s):
  result={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
  sum=0
  prev_value=0
  for i in reversed(s):
    if i in result:
      cur_value=result[i]
      if cur_value<prev_value:
        sum=sum-cur_value
      else:
        sum=sum+cur_value
      prev_value=cur_value
  return sum   
s=input()
print(RoomanToInterger(s))     
  
    

    