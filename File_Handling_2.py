file1=open("file.txt","r")
file2=open("copy.txt","w")

for line in file1:
    file2.write(line+"Hello")

file1.close()
file2.close()
