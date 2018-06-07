import time
#jobs = [[0,4,2],[1,6,4],[5,8,4],[2,10,7],[8,11,2],[9,12,1]] # job = [start,time,weight]
jobs = []
n=int(raw_input("Enter no. of jobs : "))
for i in range(n):
	joblist=[]
	start=int(raw_input("Enter start  : "))
	time=int(raw_input("Enter time : "))
	weight=int(raw_input("Enter weight : "))
	joblist.append(start);joblist.append(time);joblist.append(weight)
	jobs.append(joblist)
jobs = sorted(jobs, key = lambda x: int(x[1]))
print "Jobs : \n"jobs
p = [0]*len(jobs)
for i in range(1,len(jobs)):
    for j in range(i-1,-1,-1):
        if jobs[j][1] <= jobs[i][0]:
            p[i] = j + 1
            break
print "P: \n",p
def WIS_recursive(jobs,p,n = len(jobs)):
    val = OPT(n)
    return val
def OPT(n):
    if n == 0:
        return 0
    return max(OPT(n-1), jobs[n-1][2] + OPT(p[n-1]))
print WIS_recursive(jobs,p)