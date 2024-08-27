def BinarySearch(arr,low,high,key):
  while low<=high:
    mid=(low+high)//2
    if (arr[mid]==key):
      return mid #returns the found key index
    elif arr[mid]>key:
      high=mid-1
    else :
      low=mid+1
  return -1

if __name__ == '__main__':
  arr=[1,2,3,4,5,6,8,7,33,55]
  x=55
  n=len(arr)-1
  result=BinarySearch(arr,0,n,x)
  if result!=-1:
    print("Element found at index",result)
  else:
    print("Element not found")
