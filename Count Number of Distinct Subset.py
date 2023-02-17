from collections import Counter

def MinFrequency(Items_list):
    fredict=Counter(Items_list)
    print("Maximum number of subset:",max(fredict.values()))

if __name__=="__main__":
    Item_list=[]
    n=int(input("Give number of elements:"))
    for i in range(n):
        element=int(input("Give element"+str(i+1)+":"))
        Item_list.append(element)
    MinFrequency(Item_list) 
