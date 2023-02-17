string=input("Enter word:")

fp=open("SampleExample2.txt","w+")
fp.write("Fruits are:\n")
fp.writelines("Mango,Banana,Watermelon,Pineapple,Apple,Cucumber,")
fp.close()

fp=open("SampleExample2.txt","r")
print("The content of file before appending text was:\n",fp.read())
print()

#Using append to enter data at a line or new line
fp=open("SampleExample2.txt","a")
fp.writelines(string)
fp.close()

fp=open("SampleExample2.txt","a")
fp.write("\n")
fp.write("Fruits are good for health")
fp.close()

fp=open("SampleExample2.txt","r")
print("The content of file after appending text is:\n",fp.read())
fp.close()
print()

#Using With Statement
with open("SampleExample2.txt","a")as fp:
    fp.write("\n")
    fp.write("We should eat fruits everyday.")

with open("SampleExample2.txt","r+")as fp:
    print("The content of file after appending another line is:\n",fp.read())
