def merge(list,lb,mid,ub):
    i=lb
    j=mid+1
    k=lb
    b=[0]*len(list)
    while(i<=mid and j<=ub):
        if(list[i]<=list[j]):
            b[k]=list[i]
            i+=1
        else:
            b[k]=list[j]
            j+=1
        k+=1
    if(i>mid):
        while(j<=ub):
            b[k]=list[j]
            k+=1
            j+=1
    else:
        while(i<=mid):
            b[k]=list[i]
            k+=1
            i+=1
    for i in range(lb,ub+1):
        list[i]=b[i]

def msort(list,lb,ub):
    if(lb<ub):
        mid=(lb+ub)//2
        msort(list,lb,mid)
        msort(list,mid+1,ub)
        merge(list,lb,mid,ub)

list=[15,5,24,8,1]
lb=0
ub=len(list)-1
msort(list,lb,ub)
print(list)