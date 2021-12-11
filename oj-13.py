# from math import ceil as c
# from math import sqrt as p
# sum1 = 0
# for i in range(1, 501):
#     for j in range(2, c(p(i))):
#         if i % j != 0:
#             sum1 += i
# print(sum1)

# def func():
# #your code begin
lst = []
for i in range(2, 501):
    for j in range(2, i):
        if i % j == 0 and i > 1:
            break
    else:
        lst.append(i)
print(lst)
#     return lst
# #your code end
