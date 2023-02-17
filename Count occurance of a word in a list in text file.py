n=int(input("Enter the length of list:"))
l=[]
for i in range(n):
    String=input("Give word"+str(i+1)+":")
    l.append(String)
print()

text=open("SampleText1.txt","w+")
text.write("Letters are:\n")
text.writelines(l)
text.close()

#Count occurance of each word in a text file
with open("SampleText1.txt","r")as fp:
    print("The content of textfile is:\n",fp.read())
print()

with open("SampleText1.txt","r")as fp:
    d=dict()
    for line in fp:
        line=line.strip()
        line=line.upper()
        words=line.split(",")
        for word in words:
            if word in d:
                d[word]+=1
            else:
                d[word]=1
                
    for key in list(d.keys()):
        print(key ,":",d[key])
print()

#Count occurance of a certain word in a text file
word=input("Give want you want to find:")
count=0
with open("SampleText1.txt","r")as fp:
    for line in fp:
        line=line.upper()
        words=line.split(",")
        for i in words:
            if i==word:
                count+=1
print("Total occurance of word in the text file is: "+str(word)+":"+str(count))
print()

#Count total number of words in a text file
count=0
f=open("SampleText1.txt","r")
for i in f:
    words=line.split(",")
    count+=len(words)
print("The total number of words in the text file is:",count)    
f.close()
