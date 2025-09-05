def swap(list,a,b):
    list[a],list[b]=list[b],list[a]

def ssort(list, n):
    for i in range (n-1):
        min =i
        for j in range (i+1,n):
            if(list[j]<list[min]):
                min=j
        if(min!=i):
            swap(list,min,i)

list =[7,4,20,8,1]
n=len(list)
ssort(list,n)
print(list)