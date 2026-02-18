#pascal triangle 
n = 5 
for i in range(n):
    num = 1
    for j in range(i+1):
        print(num,end =" ")
        num = num * (i-j) // (j+1)
    print()

"""
1                   i = 0, j = 0 num = 1 so num = 1*(0-0)//(1) num = 1*0//1 so sum = 0 so printed num already so num = 1 so 1 
1 1                 i = 1 , j = 1 num = 0 so num = 
1 2 1               
1 3 3 1 
1 4 6 4 1 
"""