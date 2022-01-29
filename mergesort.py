from random import randint
from time import time
def mergesort(arr):
	if(len(arr)<=1):
		return
	mid = len(arr)//2
	L = arr[:mid]
	H = arr[mid:]
	mergesort(L)
	mergesort(H)
	i = j = k = 0
	while( i < mid and j < mid):
		if(L[i]>H[j]):
			arr[k] = H[j]
			j+=1
		else:
			arr[k] = L[i]
			i+=1
		k+=1
	while(i<mid):
		arr[k] = L[i]
		i+=1
		k+=1
	while(j<mid):
		arr[k] = H[j]
		j+=1
		k+=1
arr = [randint(0,100) for i in range(8)]
print("before sorting ",arr,sep="\n")
start = time()
mergesort(arr)
end = time()
print(f"after sorting took around {end-start}",arr,sep="\n")
