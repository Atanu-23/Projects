String=input("Enter the hyphen seperated sentence:")
l=[i for i in String.split('-')]
l.sort()
print("The sorted htphen seperated sentence is:",'-'.join(l))
