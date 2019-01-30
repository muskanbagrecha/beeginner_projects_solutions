#CHANGE CALCULATOR
change = int(input("Enter the change"))
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0
j=0
if change%1000==0:
    a+=1
elif change%500==0:
    b+=1
elif change%200==0:
    c+=1
elif change%100==0:
    d+=1
elif change%50==0:
    e+=1
elif change%20==0:
    f+=1
elif change%10==0:
    g+=1
elif change%5==0:
    h+=1
elif change%2==0:
    i+=1
else:
    j+=1
print("1000 rupee notes required are: ", a)
print("500 rupee notes required are: ", b)
print("200 rupee notes required are: ", c)
print("100 rupee notes required are: ", d)
print("50 rupee notes required are: ", e)
print("20 rupee notes required are: ", f)
print("10 rupee notes required are: ", g)
print("5 rupee notes required are: ", h)
print("2 rupee coins required are: ", i)
print("1 rupee coins required are: ", j)
