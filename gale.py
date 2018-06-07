import time
menpref=dict();womenpref=dict()
n=int(input("Enter no. of men  : "))
for i in range(n):
	print "Enter man ",i+1," : "
	man=raw_input()
	womenlist= []
	for j in range(n):
		print "Enter woman ",j+1," for the man : "
		x=raw_input()
		womenlist.append(x)
	menpref.update({man:womenlist})
for i in range(n):
	print "Enter woman ",i+1," : "
	woman=raw_input()
	menlist= []
	for j in range(n):
		print "Enter man ",j+1," for the woman"
		x=raw_input()
		womenlist.append(x)
	womenpref.update({woman:menlist})
freemen=list(menpref.keys()) ; print "Free men : ",freemen
takenwomen=[]
final={}
while freemen!=[]:
    for i in freemen:
        listofw=menpref.get(i)
        for j in listofw:
            if j not in takenwomen:
                final[j]=i
                freemen.remove(i)
                takenwomen.append(j)
                break
            else:
                listofm=womenpref.get(j)
                r=final.get(j)
                p=listofm.index(i)
                q=listofm.index(r)
                if p<q:
                    final[j]=i
                    freemen.remove(i)
                    freemen.append(r)
                    takenwomen.append(j)
                    break
print "Stable Match : ",final
print"The program ran for ",time.clock()," seconds"
