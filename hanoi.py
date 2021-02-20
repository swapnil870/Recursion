def hanoi(n,source,temp,dest):
    if n==1:
        print("Move disk from",source,"to",dest)
    elif n==0:
        pass
    else:
        hanoi(n-1,source,dest,temp)
        print("Move disk from",source,"to",dest) 
        hanoi(n-1,temp,source,dest)
def main():
    n=int(input("Enter number of disk:"))
    source=int(input("Enter number source:"))
    temp=int(input("Enter number temporary:"))
    dest=int(input("Enter number destination:"))
    hanoi(n,source,temp,dest)
name="main"
if name=="main":
    main()


