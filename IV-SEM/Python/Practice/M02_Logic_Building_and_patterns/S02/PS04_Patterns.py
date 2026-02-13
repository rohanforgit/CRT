n = 5
m = n
print()
print("Square Pattern")
print()

for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end =" ")
    print()

print()
print("Triangle Pattern")
print()
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end = " ")
    print()
print()

print("Inverted Triangle")
print()
for i in range(n):
    for j in range(i,n):
        print("*",end = " ")
    print()



print("Numbered Triangle")

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end = " ")
    print()

print()
print("Numbered Trisngle Same Number")
print()

for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end = " ")
    print()

print()
print("Alphabet Triangle")
for i in range(n):
    for j in range(i+1):
        print(chr(65+j),end = " ")
    print()
print()

floyd = 0
print("Floyd triangle")
for i in range(0,n):
    for j in range(0,i):
        floyd+=1
        print(floyd,end = " ")
    print()
print()

print("Hollow")
for i in range(n):
    for j in range(m):
        if i==0 or i ==n-1 or j==0 or j==m-1:
            print("*",end =" ")
        else:
            print(" ",end =" ")
    print()

