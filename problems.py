import math
from queue import LifoQueue,Queue
def result_set(l,k):
	sl=list(set(l))
	count=0
	for i in range(0,len(sl)):
		count=binarySearch(sl,sl[i]+k,i+1,len(sl)-1,count)
	print(count)
def binarySearch(sl,t,i,n,count):
	if i>n:
		return count
	mid=(i+n)//2
	#print(sl[mid])
	if t>sl[mid]:
		return binarySearch(sl,t,mid+1,n,count)
	elif t<sl[mid]:
		return binarySearch(sl,t,i,mid,count)
	elif t==sl[mid]:
		count+=1
		return count
l=[1,1,1,2]
k=1
result_set(l,k)
def minsum(l,c):
	if c==0:
		return l
	m=max(l)
	k=math.ceil(m/2)
	l[l.index(m)]=k
	return minsum(l,c-1)
l=[10,20,7]
k=4
print(minsum(l,k))
def reomove_k_cons(string,k):
	st=[]
	st.append(string[0])
	count=1
	for i in range(1,len(string)):
		
	return 
string="abbcccbd"
print(reomove_k_cons(string,3))
