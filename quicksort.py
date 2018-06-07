import time
import random
L = []
for i in range(20):
	L.append(random.randint(0,200))
n=len(L)
print "Unsorted List : \n",L
def partition(arr,low,high):
	i=low-1
	pivot=arr[high]
	for j in range(low,high):
		if arr[j]<=pivot:
			i=i+1;arr[i],arr[j]=arr[j],arr[i]
	arr[i+1],arr[high]=arr[high],arr[i+1]
	return i+1
def quicksort(arr,low,high):
	if low<high:
		pi=partition(arr,low,high)
		quicksort(arr,low,pi-1)
		quicksort(arr,pi+1,high)
start=time.clock()
quicksort(L,0,n-1)
end=time.clock()
print "Sorted List : \n",L,"\nTime taken to sort list using Quicksort : ",end-start," seconds"