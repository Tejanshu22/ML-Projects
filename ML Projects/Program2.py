string = input("Enter string")
d = 0
st = list(string)
diff = list()
for i in range(0, len(st)):
    for k in range(i + 1, len(st)):
        if st[i] == st[k]:
            p1 = i
            p2 = k
            d = p2 - p1
            diff.append(d)
diff.sort()
x = diff[-1] - 1
print(x)