print("This is aprogram to copy a content of one file to another")
print()
print("Press 1 for using read and append method to copy a file")
print()
print("Press 2 for using read and write method to copy a file")
print()
print("Press 3 for using shutil.copy() method to copy a file")
print()
n=int(input("Enter your choice:"))
if n==1:
    with open("SampleText1.txt","r")as fp,open ("SampleText2.txt","a")as sp:
        lines=fp.readlines()
        lines_seen=set()
        for line in lines:
            if line not in lines_seen:
                lines_seen.add(line)
            sp.write(str(lines_seen))
            
    with open("SampleText2.txt","r")as sp:
        print("Content of Second file:\n",sp.read())


elif n==2:
    with open("SampleText1.txt","r")as fp,open ("SampleText3.txt","w")as sp:
        for line in fp:
            sp.write(line)
    with open("SampleText3.txt","r")as sp:
        print("Content of Second file:\n",sp.read())        


elif n==3:
    import shutil
    shutil.copyfile("SampleText1.txt","SampleText4.txt")

    with open("SampleText4.txt","r")as sp:
        print("Content of Second file:\n",sp.read())
    
                                                       
else:
    print("Default Input")
