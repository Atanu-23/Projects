file1=open("Text2.txt","w+")
n=int(input("Give number of Words:"))
l=[]
for i in range(n):
    string=input("Give String"+str(i+1)+":")
    l.append(string)
file1.writelines(l)
file1.close()
print()

with open("Text2.txt","r+")as fp:
    print("Contents of file is:\n",fp.read())
print()

file1=open("ReverseText1.txt","w+")
with open("Text2.txt","r+")as myfile:
    letter=myfile.read()
letter_reverse=letter[::-1]
file1.write(letter_reverse)
file1.close()

with open("ReverseText1.txt","r")as mfp:
    print("Contents of file in reverse order:",mfp.read())
    print()

