def test(strs):
  res=''
  for i in range(len(strs[0])):
    for s in strs[0]:
      if i==len(s) or s[i]!=strs[0][i]:
        return res
    res=res+str[0][i]  