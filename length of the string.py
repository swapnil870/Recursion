def string(n):
    if n=="":
        return 0
    else:
        return len(n[0:])
    '''else:
        return 1+len(n[1:])'''

def main():
    n=input("Enter a string:")
    result=string(n)
    print("The length of the given string",n,"is",result)
name="main"
if name=="main":
    main()
