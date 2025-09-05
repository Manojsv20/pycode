def linear(list,key):
    n=len(list)
    for i in range(n):
        if(list[i]==key):
            print("the value {} is found in the index of {}".format(list[i],i))
            return 0
    print("the element is not found")
list=[7,3,90,57,9]
key=57
linear(list,key)
