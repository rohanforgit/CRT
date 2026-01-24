# lis = [1,2,3,4,5]
# rohan = 0
# for i in range(len(lis)):
#     rohan += lis[i]%10
    
# print(rohan)

li = [1,2,3,4,5]
li2 = []
num = 0
for i in li:
    num =  num%10
num = num+1

while num>0:
    li2.append(num%10)
    num//=10
li2.reverse()
print(li2)
# num = 1234
# print(num%10)
# num //=10
# print(num%10)
# num //=10
# print(num%10)

# li1 = [1,2,3,4]
# li = []
# while len(li1)>0:
#     li.append(li1[i]%10)
#     li[i]//=10
# li.reverse()
# print(li)