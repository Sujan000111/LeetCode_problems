def SubstringsK(s,k):
  n=len(s)
  for i in range(n-k+1):
    sub_array=s[i:i+k]
    unique_chars=set(sub_array)
    if len(unique_chars)==k:
      print(sub_array)
s=input()
k=int(input())
SubstringsK(s,k)       


def SubstringsK(s, k):
    n = len(s)
    print(f"Substrings with exactly {k} distinct characters:")

    for i in range(n):
        unique_chars = set()
        sub_string = ""

        for j in range(i, n):
            unique_chars.add(s[j])
            sub_string += s[j]

            if len(unique_chars) == k:  # Print only when we reach exactly k distinct chars
                print(sub_string)
            elif len(unique_chars) > k:  # Stop if more than k distinct characters are found
                break  

s = input()
k = int(input())
SubstringsK(s, k)

  