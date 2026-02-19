def even_odd(n: int) -> str:
   pass
   if n%2!=0:
       return "Weird"
   elif n==2 or n==4:
       return "Not Weird"
   elif n%2==0 and n>=6 and n<=20:
       return "Weird"
   elif n%2==0 and n>20:
       return "Not Weird"
'''If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
Input Format'''

if __name__ == '__main__':
    n = int(input())
    print(even_odd(n))
