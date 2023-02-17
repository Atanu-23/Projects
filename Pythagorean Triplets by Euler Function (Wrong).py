limit=int(input("Enter range: "))
def Pythagorean_Triplets(limit):
    c=count=0
    m=2
    while c<limit:
        for n in range(1,m):
            a=(m*m-n*n)
            b=2*m*n
            c=(m*m+n*n)
            if c>limit:
                break
            print("Pythagorean Triplets are: ",a,b,c)
            count=count+1
        m=m+1
    print("Number of Pythagorean triplets are: ",count)
Pythagorean_Triplets(limit)     

