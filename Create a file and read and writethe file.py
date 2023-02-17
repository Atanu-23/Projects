L=["This is mango\nThis is orange\nThis is pineapple\n"]
with open('myfile2.txt','w')as fp:
    fp.write("Hello\n")
    fp.writelines(L)
    fp.close()
    
with open('myfile2.txt','r+')as fp:
    print("Output of read function is:")
    print(fp.read())


with open('myfile2.txt','r+')as fp:
    print("Output of readline function is:")
    print(fp.readline(5))


with open('myfile2.txt','r+')as fp:
    print("Output of readlines function is:")
    print(fp.readlines())
