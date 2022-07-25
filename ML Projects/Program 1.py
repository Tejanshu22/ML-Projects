times = int(input("Number of times "))
L = list()
e = int(input("Number "))
for t in range(0, times):
    command = input("Command ")
    if command == "insert":
        i = int(input("Position "))
        n = int(input("Number "))
        L.insert(i, n)
        print(L)
    if command == "remove":
        L.remove(e)
    if command == "append":
        L.append(e)
    if command == "sort":
        L.sort()
        print(L)
    if command == "pop":
        L.pop()
    if command == "reverse":
        L.reverse()
        print(L)