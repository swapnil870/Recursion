def reverse(n):
    if n=="":
        return n
    else:
         return n[-1]+reverse(n[:-1])
def main():
    n=input("Enter a string to get reverse")
    result=reverse(n)
    print("The reverse of string",n,"is",result)
name="main"
if name=="main":
    main()
