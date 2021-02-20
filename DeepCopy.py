def deepCopy(lst1,lst2=[]):
    if lst1==[]:
        pass
    else:
        if type(lst1[0])!=list:
            lst2.append(lst1[0])
        else:
            lst2.append([])
            deepCopy(lst1[0],lst2[-1])
        deepCopy(lst1[1:],lst2)
    return lst2
def main():
    lst1=eval(input("Enter a list:"))
    lst2=deepCopy(lst1)
    print("Deep copy of list lst1 is",lst2)
name="main"
if name=="main":
    main()
