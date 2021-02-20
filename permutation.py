def permutation(word):
    if len(word)==1:
        return word
    l=[]
    for i in range(len(word)):
        s=permutation(word[0:i]+word[i+1:])
        for j in s:
            l.append(word[i]+j)
    return l
def main():
    word=input("Enter the value:")
    result=permutation(word)
    print(result)
name="main"
if name=="main":
    main()
    
            
