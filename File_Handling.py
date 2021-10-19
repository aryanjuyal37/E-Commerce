# f=open("File.txt","r")
# print(f.read())

# print(f.readline(),end="abs")
# print(f.readline())

# print(f.readlines())
# f.close()

with open("File.txt","r") as f:
    print(f.readlines())#automatically closes  