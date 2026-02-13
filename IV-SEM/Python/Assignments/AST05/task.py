from typing import List


def Collatz_Sequence(n: int)-> List:
   pass
   li = [n]
   while n!=1:
       if n%2==0:
           n//=2 
       else:
           n = 3*n+1
       li.append(n)
   return li
 

if __name__ == '__main__':
    n = int(input())
    print(Collatz_Sequence(n))