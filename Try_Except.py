try:
    price=int(input("Enter the price-"))

except:
    print("Invalid Input")

else:
    print("Product added successfully")


try:
    print(2/0)

except:
    print("Zero division error")

else:
    print("Division Successful")

finally:
    print("Perhaps")