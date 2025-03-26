def rotateString(a, r=2):
    n = len(a)
    r = r % n  # Handle cases where r > n
    rotated = a[r:] + a[:r]  # Slice and concatenate
    print(rotated)

a = input("Enter a string: ")
rotateString(a)

