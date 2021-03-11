def reverseArray(arr,start,end):
    while(start<end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end = end-1
def leftRotate(arr, d):
    n = len(arr)
    reverseArray(arr,0,d-1)
    reverseArray(arr,d,n-1)
    reverseArray(arr,0,n-1) 
def printArray(arr):
    for i in range(0, len(arr)):
        print(arr[i])
if __name__ == "__main__":
    arr = [1,2,3,4,7,10,11,12]
    leftRotate(arr, 5)
    printArray(arr)
