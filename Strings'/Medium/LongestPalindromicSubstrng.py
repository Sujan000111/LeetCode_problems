def PalindromicSubstring(s):
  n=len(s)
  result=[]
  max_substring=''
  for i in range(n):
    for j in range(i,n):
      sub_string=s[i:j+1]
      reverse_sub_string=sub_string[::-1]
      if sub_string==reverse_sub_string:
        result.append(sub_string)
  return max(result,key=len)    
s=input()
print(PalindromicSubstring(s))
    