from collections import Counter
String=input('Give the string:')
coun=Counter(String)
print(coun)   
print("\n")

for i in coun.elements():
    print(i,end=" ")
print("\n")
for m in coun.elements():
    print("%s:%s"%(m,coun[m]),end="\n")
print("\n")    

n=int(input("Give length:"))
l=[]
for j in range(n):
    e=int(input("Give number"+str(j+1)+":"))
    l.append(e)
coun=Counter(l)
print(coun)
for k in coun.elements():
    print(k,end=" ")
print("\n")
for m in coun.elements():
    print("%s:%s"%(m,coun[m]),end="\n")
print("\n")



