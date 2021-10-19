x=input("Enter price of 1st item- ")
y=input("Enter price of 2nd item- ")
add= int(x)+int(y)
tax=add*0.1
total=add+tax

if total>=1000:
    total=total-total*0.1

elif total>=500 and total<100:
    total=total-total*0.7

else:
    pass

print(total)  