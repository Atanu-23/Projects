print("This is a program to find the length of list using recursion")
print()
print("Press 1 for first process")
print()
print("Press 2 for second process")
print()
n=int(input("Enter your choice:"))
print()
my_list=[1,3,5,7,2,8,4,9,2,7,9,4,0,3,6,3,1,4,3,6,8,3,1,9,0,8,9,1,4]
print(my_list)
print()
if n==1:
    def Lengthlist(l):
        if not l:
            return 0
        return 1+Lengthlist(l[1:])
    print("The length of list is:",Lengthlist(my_list))
elif n==2:
    length=0
    def lengthlist(a):
        global length
        if a:
            length = length + 1
            lengthlist(a[1:])
        return length
    print("The length of list is:",lengthlist(my_list))
else:
    print("Default Input.Please enter choice 1 or choice 2!!")
    
