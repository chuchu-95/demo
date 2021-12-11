a = []
d = [3, 2, 1, 1]
for i in d:
    if i not in a:
        a.append(i)
a.sort()
print(a)
