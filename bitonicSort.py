
def bitonicmerge(tab,starting,k,direction):
	if(k<1):
		return
	print("from ",tab[starting:starting+k*2],end=" ")
	for i in range(starting,starting+k):
		if(tab[i]>tab[k+i])==direction:
			tab[i],tab[i+k] = tab[i+k],tab[i]
	print("to ",tab[starting:starting+2*k],direction)
	bitonicmerge(tab,starting,k//2,direction)
	bitonicmerge(tab,starting+k//2+1,k//2,direction)


def bitonicsort(tab,starting,k,direction):
	if(k<1):
		return
	m=k//2
	bitonicsort(tab,starting,m,True)
	bitonicsort(tab,starting+m,m,False)
	bitonicmerge(tab,starting,m,direction)
	#print(tab[starting:starting+k],direction)




tab = [int(input(f"enter the {i}'th element :")) for i in range(8)]

#the algorithms only work for tables with length of 2^n

bitonicsort(tab,0,8,True)
print(tab)
