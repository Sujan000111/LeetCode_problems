def generate_permutations(a,start,end,result):
  
  if start==end:
    result.append(a[:])
  

  else:
    for i in range(start,end):
      a[start],a[i]=a[i],a[start]
      generate_permutations(a,start+1,end,result) 
      a[start],a[i]=a[i],a[start]
     

def Permutations(a):
  result=[]
  generate_permutations(a,0,len(a),result)
  return result

def input_format():
  a=list(map(int,input().strip("[]").split(",")))
  print(Permutations(a))
input_format()  