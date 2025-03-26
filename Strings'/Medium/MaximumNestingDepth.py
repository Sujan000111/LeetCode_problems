def MaximumNestingDepth(s):
  cur_depth=0
  max_depth=0
  for i in s:
    if i =="(":
      cur_depth=cur_depth+1
      max_depth=max(max_depth,cur_depth)
    elif i==")":
      cur_depth=cur_depth-1
  return max_depth
s=input()
print(MaximumNestingDepth(s))    