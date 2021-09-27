def linearSearch(array):
    key=6
    count=0
    for i in range(len(array)):
        if array[i]==key:
            count+=1
            break

    if count==1:
        print("Element found in array")
    else:
        print("Element not found in array")
          
if __name__=="__main__":
    array=[1,4,3,6,8,9,22,10]
    linearSearch(array)
    
