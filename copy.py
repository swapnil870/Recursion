def copy(lst1,lst2=[]):
    if lst1==[]:
        return lst2
    else:
        lst2.append(lst1[0])
        copy(lst1[1:],lst2)
    return lst2
def main():
    lst1=eval(input("Enter the list:"))
    lst2=copy(lst1)
    print("copy of list lst1 is",lst2)
name="main"
if name=="main":
    main()


        
