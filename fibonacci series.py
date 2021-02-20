'''def fibonacci(n):
    f=0
    s=1
    if n==0:
        print(f,s)
    elif n==1:
        print(f)
    else:
        for i in range(2,n+1):
            t=f+s
            f=s
            s=t
    return s
def main():
    n=int(input("Enter a integer number:"))
    result=fibonacci(n)
    print("Fibonacci series",n,"is",result)
name="main"
if name=="main":
    main()'''
def fibonacci(n):
    assert n>0
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci (n-2)
def main():
    n=int(input("Enter a integer number:"))
    result=fibonacci(n)
    print("Fibonacci series",n,"is",result)
name="main"
if name=="main":
    main()
    
