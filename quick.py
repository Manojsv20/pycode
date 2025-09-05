def part(list,lb,ub):
    pivot=list[lb]
    start=lb
    end=ub
    while(start<end):
        while (start<=ub) and (list[start]<=pivot):
            start+=1
        while(list[end]>pivot):
            end-=1
        if(start<end):
            list[start],list[end]=list[end],list[start]
    list[lb],list[end]=list[end],list[lb]
    return end 


def qsort(list,lb,ub):
    if(lb<ub):
        loc=part(list,lb,ub)
        qsort(list,lb,loc-1)
        qsort(list,loc+1,ub)

list=[7,6,10,5,9,2,1,15,7]
lb=0
ub=len(list)-1
qsort(list,lb,ub)
print(list)