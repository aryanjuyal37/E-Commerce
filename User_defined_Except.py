class Marksoutofbound(exception):
    def __init__(self,arg):
        self.message=arg

def validateMarks():
    if marks>100:
        raise Marksoutofbound("Please enter marks less than 100 ")


try: 
    marks=int(input("Enter marks"))
    validatemarks(marks)

except Marksoutofbound as err:
    print(err)

else:
    print("Valid")