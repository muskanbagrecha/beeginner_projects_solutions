#MUSKAN BAGRECHA
def Pythagorean_triplets(a,b,c):
    z=0
    if a>b and a>c:
        if a**2 == b**2 + c**2:
            z=1
    elif b>a and b>c:
        if b**2== a**2 + c**2:
            z=1
    else:
        if c**2==a**2+b**2:
            z=1
    if z==1:
        print("It is a Pythagorean Triplet")
    else:
       print("It is not a Pythagorean Triplet")
#MAIN
while True:
    choice = int(input("Do you want to check for Pythagorean triplet? Enter 1 for yes and 0 for no"))
    if choice==0:
        print("thank you")
        break
    n = input("Enter the sides separated by a space")
    a, b, c = n.split()
    a1=int(a)
    b1=int(b)
    c1=int(c)
    Pythagorean_triplets(a1, b1, c1)
    
