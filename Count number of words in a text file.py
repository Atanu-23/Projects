file1=open("SampleExample1.txt",'w+')
file1.write("Hello World!\n")
l=["I'm python\nI'm a first developing language\nI use many library function\n"]
file1.writelines(l)
for i in range(4):
    file1.write("I'm Python\n")
file1.write("Number: 4\n")
file1.write("Number: 25\n")
file1.write("Number: 64")
file1.close()

#Read the text file
with open("SampleExample1.txt","r+")as file:
    print("The content of file is:\n",file.read())

print()

#Count number of lines using readlines
with open("SampleExample1.txt",'r')as fp:
    totallines=len(fp.readlines())
    print("Number of lines in the text file is:",totallines)

#Count number of words with all value    
number_of_words=0
with open("SampleExample1.txt","r+") as file:
    data=file.read()

    lines=data.split()
    number_of_words+=len(lines)
print("Number of words in text file is:",number_of_words)

print()

#Count number of lines using enumerate
count=0
with open("SampleExample1.txt","r")as fp:
    for count,lines in enumerate(fp):
        pass
    print("Number of lines in the text file is:",count+1)
    
#Count number of words without any numeric value
number_of_words=0
with open("SampleExample1.txt","r+")as file:
    data=file.read()

    lines=data.split()
    
    for word in lines:
        if not word.isnumeric():
            number_of_words+=1
print("Number of words without any numeric value is:",number_of_words)

print()

#Count number of lines using forloop and counter
file=open("SampleExample1.txt","r")
counter=0
content=file.read()
contentlist=content.split("\n")
for i in contentlist:
    if i:
        counter+=1
print("The number of lines in the text file is:",counter)

print()

#Count number of lines using sum function and forloop
with open("SampleExample1.txt",'r')as fp:
    lines=sum(1 for line in fp)
    print("The number of lines in the text file is:",lines)
