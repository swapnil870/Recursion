def palindrome(n):
    if n=="":
        return True
    else:
        return (n[0]==n[-1]) and palindrome(n[1:-1])
def main():
    n=input("Enter a String to get palindrome")
    if palindrome(n):
        print("String is palindrome")
    else:
        print("string is not palindrome")
name="main"
if name=="main":
    main()
