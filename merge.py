import time
import random
def mergesort(list1):
	if len(list1) > 1:
		mid=len(list1)/2
		lefthalf=list1[:mid]
		righthalf=list1[mid:]
		mergesort(lefthalf)
		mergesort(righthalf)
		i=0;j=0;k=0;
		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] <= righthalf[j]:
				list1[k]=lefthalf[i]
				i=i+1; k=k+1
			elif righthalf[j] <= lefthalf[i]:
				list1[k]=righthalf[j]
				j=j+1; k=k+1
		while i < len(lefthalf) :
			list1[k] = lefthalf[i]
			i=i+1 ; k=k+1
		while j < len(righthalf):
			list1[k] = righthalf[j]
			j=j+1 ; k=k+1
	#print "Merging",list1
L = []
for i in range(20):
	L.append(random.randint(0,200))
print "Unmerged List : \n", L
start=time.clock()
mergesort(L)
end=time.clock()
print "Merged List :\n",L
print "Time taken to merge list : ",(end-start)," seconds"