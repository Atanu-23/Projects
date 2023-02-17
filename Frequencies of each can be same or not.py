from collections import Counter

def AllSame(input_data):
    dictionary=Counter(input_data)

    same=list(set(dictionary.values()))

    if len(same)>2:
        print("No")
    elif len(same)==2 and same[1]-same[0]>1:
        print("No")
    else:
        print("Yes")

if __name__=="__main__":
    input_data=input("Enter data:")
    AllSame(input_data)
