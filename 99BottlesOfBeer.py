def beer_bottles(n):
    if n==0:
        return "No more bottles"
    elif n==1:
        return "1 bottle"
    else:
        return str(n)+" bottles"
#main

n=99
while(n>=0):
    print(beer_bottles(n)+" of beer on the wall, " + beer_bottles(n) + " of beer.")
    if n==0:
        print("Go to the store and buy some more, " + beer_bottles(99) +" of beer on the wall \n")
    else:
        print("Take one down and pass it around, " + beer_bottles(n-1) + " of beer on the wall. \n")
        
    n=n-1
