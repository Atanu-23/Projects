file1=open('Myfile.txt','w')
file1.write("Hello world,I'm Python\n")
l=["I'm a first developing language\nI use many inbuild library function\n"]
file1.writelines(l)
for i in range(4):
    file1.write("Hello World\n")
file1.close()

file1=open('Myfile.txt','r+')
print("Output of read function is:\n")
print(file1.read())
print()
file1.seek(0)

print("Output of readline function is:\n")
print(file1.readline(7))
print()
file1.seek(0)

print("output of readlines function is:\n")
print(file1.readlines())
print()


