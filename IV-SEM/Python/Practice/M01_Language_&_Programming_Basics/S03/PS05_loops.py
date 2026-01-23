# n = int(input("Enter a Digit : "))
# count = 0
# if n==0:
#     count = 1
# while n>0:
#     count += 1
#     n = n//10

# print(count)
'''
# n = int(input("Enter a Digit : "))
# count = 0
# for count in range(0,5,1):
#     print("hello world") 
'''
'''
li = [1,2,3,4,5]
for i in range (1,len(li),1):
    li[i]=li[i]**2
print(li)


'''

'''
lirohan = [0,1,2,3,4,5,6]
for i in range(0,len(lirohan),2):
    print(lirohan[i],end =",")
'''


# n = input()

# lst = ['a','e','o','i','u']
# count = 0
# for i in range (len(n)):
#     if n[i] in lst:
#         count+=1
# print(count)

'''
s = input()
count = 0
for ch in s:
    if ch in    "aeiouAEIOU":
        count+=1
print(count)
'''

# for i in range(1,11):
#     if i == 5:
#         break
#     print(i,end=" ")

# for i in range(1,11):
#     if i == 5:
#         continue
#     print(i,end=" ")


password = "rohan123"
tries = 4
for _ in range(3):
    n = input()
    if n==password:
        print("Correct Password")
        break
    else:
        # tries-=1
        print("Wrong password attempt")
        continue
