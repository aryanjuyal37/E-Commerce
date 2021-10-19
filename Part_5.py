# for i in range(0,10,2):
#     print(i)

# for y in [1,23.5]:
#     print(y)

option= True
data={}
while option:
    print("1. Update items")
    print("2. Show items")
    print("3. Exit")
    choice=input("Enter choice-")

    if choice=="1":
        item_name=input("Enter name of item-")
        item_quantity=input("Enter quantity-")
        data[item_name]=item_quantity

    elif choice=="2":
        for i,j in data.items():
            print(i,j)

    elif choice=="3":
        print("Ending")
        option= False
    
    else:
        print("Invalid choice")

    