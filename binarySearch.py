def binarySearch(array,item):
   
    low=0
    
    high=len(array)-1

    count =False
    
    while low<=high:
        
        mid=(low+high)//2
        
        if array[mid]==item:
            count=True
            print(f"Item found at {mid+1} index")
            break
        
        elif array[mid]>item:
            high=mid-1
            
        else:
            low=mid+1


    if count == False:
        print("Not Found in Array")


if __name__=="__main__":
    
    array=[1,2,3,4,5,6,7,8,9,10]
    
    item=10
    
    binarySearch(array,item)
