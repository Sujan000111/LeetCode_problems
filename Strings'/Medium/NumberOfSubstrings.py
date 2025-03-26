def NumberOfSubStrings(s):
  count=0
  for i in range(len(s)):
    for j in range(i,len(s)):
      sub_string=s[i:j+1]
      count=count+1
  return count
s=input()
print(NumberOfSubStrings(s))      


