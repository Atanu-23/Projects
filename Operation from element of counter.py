from collections import Counter

#With sequence of item using list
l=[]
n=int(input("Enter length of list:"))
for i in range(n):
    element=input("Give element"+str(i+1)+":")
    l.append(element)
print("The counter made from list is:",Counter(l))
print(Counter(l).items())
print("Sum of elements of values of counter is:",sum(Counter(l).values()))
