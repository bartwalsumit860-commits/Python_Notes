#program to identify the largest number between three numbers
def largest(a,b,c):
    if a>b and a>c:
        return 'a' 
    elif b>a and b>c:
        return 'b'
    else: return 'c'


a = int(input("enter a: "))
b = int(input("enter b: "))
c = int(input("enter c: "))

print(f"largest number is {largest(a,b,c)}")