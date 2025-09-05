def isort(list,n):
    for i in range (n):
        temp=list[i]
        j=i-1
        while (j>=0) and (list[j]>temp):
            list[j+1]=list[j]
            j-=1
        list[j+1]=temp
        
list =[7,4,20,8,1]
n=len(list)
isort(list,n)
print(list)