def bin (list,key):
    lb=0
    ub=len(list)-1
    while(lb<=ub):
        mid=(lb+ub)//2
        if(list[mid]==key):
            print(f"element {list[mid]} is found in {mid}")
            return 0
        elif(key>list[mid]):
            lb=mid+1
        else:
            ub=mid-1
    print("the key is not found")
list =[1,2,3,4,5,6,8,9,10]
key=13
bin(list,key)
