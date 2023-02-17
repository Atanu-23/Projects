file1=open("Text3.txt","w+")
n=int(input("Give number of Words:"))
l=[]
for i in range(n):
    string=input("Give String"+str(i+1)+":")
    l.append(string)
    l.append('\n')
file1.writelines(l)
file1.close()
print()

with open("Text3.txt","r+")as fp:
    print("Contents of file is:\n",fp.read())
print()


file1=open("ReverseText2.txt","w+")
with open("Text3.txt","r+")as myfile:
    word=myfile.readlines()
word_reverse=word[::-1]
file1.writelines(word_reverse)
file1.close()

with open("ReverseText2.txt","r")as nfp:
    print("Contents of file in word to word reverse order:",nfp.read())
    print()

