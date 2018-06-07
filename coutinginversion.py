import time
import random
L= []
n=int(raw_input("Enter range of array : "))
for i in range(n):
	print "Enter element ",i+1,"of the array : "
	L.append(int(raw_input()))
print "Array :",L
def inversion(list1,n):
	count=0;
	for i in range(n):
		for j in range(i+1,n):
			if(list1[i]>list1[j]):
				count=count+1
	print "No. of inversions for the given array : ",count
start=time.clock()
inversion(L,len(L))
end=time.clock()
print "Time taken to count no. of inversions : "(end-start)," seconds"