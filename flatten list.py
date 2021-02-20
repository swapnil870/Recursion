def flattenlist(lst1,lst2=[]):
    for i in lst1:
        if type(i)!=list:
            lst2.append(i)
        else:
            flattenlist(i,lst2)
    return lst2
def main():
    lst1=eval(input("Enter list:"))
    result=flattenlist(lst1)
    print("Flatten List:",result)
name="main"
if name=="main":
    main()
