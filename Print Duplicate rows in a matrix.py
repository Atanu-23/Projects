from collections import Counter


def Duplicate(input1):
    input2=map(tuple,input1)

    freqDict=Counter(input2)

    for (row,freq)in freqDict.items():
        if freq>1:
            print(row)

if __name__ == "__main__":
    print("The Matrix is:")
    n=int(input("Enter number of list:"))
    list1=[]
    list2=[]
    for i in range(n):
        for j in range(n):
            e=int(input("Enter element"+str([j])+":"))
            list1.append(e)
        list2.append(list1)
        list1=[]
    for j in list2:
        print(j,"\n")

    input1=list2
    Duplicate(list2)
