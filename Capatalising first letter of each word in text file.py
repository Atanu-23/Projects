file1=open("Text1.txt","w+")
n=int(input("Enter number of string:"))
l=[]
for i in range(n):
    string=input("Enter string"+str(i+1)+":")
    l.append(string)
file1.write("contents are:\n")
file1.writelines(l)
file1.close()
print()

with open("Text1.txt","r+")as fp:
    print("Contents of file is:\n",fp.read())
print()

#Capatalise first letter of each word using title() function
with open("Text1.txt","r+")as fp:
    for line in fp:
        output_file=line.title()
    print("After Capatalising first letter of each word:\n",output_file)
print()

#Capitalise first letter of each word using capitalize() functuion
with open("Text1.txt","r+")as fp:
    data=fp.read()
    line=data.split()
    print("After Capatalising first letter of each word:\n")
    for i in line:
        print(i.capitalize(),end=" ")
        if i.capitalize()=="Are:":
            break
    print()
    words=line[-1].split(",")
    for word in words:
        if word==words[-1]:
            print(word.capitalize())
            break
        else:
            print(word.capitalize(),end=",")
print()            

#Capitalise first letter of each word using string slicing and upper method
with open("Text1.txt","r+")as fp:
    data=fp.read()
    lines=data.split()
    print("After Capatalising first letter of each word:\n")
    words=lines[-1].split(",")
    for line in lines:
        con=line[0].upper()+line[1:]
        print(con,end=" ")
        if con=="Are:":
            break
    print()
    for word in words:
        if word==words[-1]:
            print(word[0].upper()+word[1:])
            break
        else:
            print(word[0].upper()+word[1:],end=",")
print()

#Capitalise first letter of each word using join,split and capitalize function
with open("Text1.txt","r+")as fp:
    data=fp.read()
    lines=data.split()
    print("After Capatalising first letter of each word:\n")
    words=lines[-1].split(",")
    for word in lines:
        result=' '.join(element.capitalize() for element in word.split())
        print(result,end=" ")
        if result=="Are:":
            break
    print()
    for word in words:
        result=" ".join(elem.capitalize() for elem in word.split())
        if word==words[-1]:
            print(result)
            break
        else:
            print(result,end=",")
print()

#Capitalise first letter of each word using string.capwords() function
import string
with open("Text1.txt","r+")as fp:
    data=fp.read()
    lines=data.split()
    print("After capitalising first letter of each word:\n")
    words=lines[-1].split(",")
    for word in lines:
        result=string.capwords(word)
        print(result,end=" ")
        if result=="Are:":
            break
    print()
    for word in words:
        result=string.capwords(word)
        if word==words[-1]:
            print(result)
            break
        else:
            print(result,end=",")
print()            
