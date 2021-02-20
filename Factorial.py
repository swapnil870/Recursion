# Factorial of the number with genral method
'''def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
def main():
    n=int(input("Enter the number to get factorial:"))
    result=factorial(n)
    print("Factorial of the number",n,"is",result)
name="main"
if name=="main":
    main()'''
#Factorial of the number with recursion method
def factorial(n): 
     assert n>=0
     if n==0 or n==1:
         return 1
     else:
        return n * factorial(n-1)
def main():
    n=int(input("Enter a number to get factorial"))
    result=factorial(n)
    print("Factorial of the number",n,"is",result)
name="main"
if name=="main":
    main()

    
