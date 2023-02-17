fp=open("Textfile2.txt","w+")
n=int(input("Enter number of characters:"))
l=[]
for i in range(n):
    character=input("Enter word"+str(i+1)+":")
    l.append(character)
fp.write("This file has:\n")
fp.writelines(l)
fp.close()
print()

with open("Textfile2.txt","r")as file:
    print("Contents of file is:\n",file.read())
print()
    
print("Press 1 for using isspace() function to count number of spaces")
print()
print("Press 2 for using for loop to count number of spaces")
print()
print("Press 3 for using python module functool to count number of spaces")
print()
a=int(input("Enter your choice:"))
print()

#using isspace() function to count number of spaces
if a==1:
    with open("Textfile2.txt","r")as fp:
        count=-1
        while True:
            char=fp.read(1)
            if char.isspace()==True:
                count+=1
            if not char:
                break
    print("Number of spaces in the text file is:",count)
    print()
      
#using for loop to count number of spaces
elif a==2:
    with open("Textfile2.txt","r")as fh:
        count=0
        while True:
            char=fh.read(1)
            if char==" ":
                count+=1
            if not char:
                break
    print("Number of spaces in the text file is:",count)
    print()

#using python module functool to count number of spaces
    # Not Working
elif a==3:
    import functools
    spaces=0
    with open("Textfile2.txt")as file:
        file_char=functools.partial(file.read, 1)
        for char in iter(file_char," "):
            if char==" ":
                spaces+=1
    print("Number of spaces in the text file is:",spaces)            
    print()        

else:
    print("Default input!!!")
