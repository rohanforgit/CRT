# # n = int(input())
# # n = 5
# # print("Pyramid Pattern")
# # for i in range(1,n+1):
# #     for j in range(i):
# #         print(" * ",end = " ")
# #     print(" ")

# '''li = [1,2,3,4,5]
# lis = []
# for i in li:
#     if i%2==0:
#         lis.append(i)
# print(lis)
# print([ele**2 for ele in li])
# print([i for i in li if i%2==0])'''

# li1 = ['a','b','c']
# ro = " "
# for i in li1:
#     ro = ro+ i+" "
# print(ro)

# print(" ".join(li1))

#pyramid pattern
# n = 2
# for i in range(1,n+1):
#     print(" " * (n - i)+"* "*i)
# for i in range(n,0,-1):
#     print(" " * (n - i)+"* "*i)

n = 5 
for i in range(n,0,-1):
    print(i,end = "") 
    for j in range(2,n+1,1):
        print(j,end ="")
    print()
 