import time
graph=dict()
n=int(input("Enter no. of nodes : "))
for i in range(n):
	node=int(raw_input("Enter node : "))
	x=int(input("Enter no. of nodes connected to the given node : "))
	edge=[]
	for j in range(x):
		print "Enter node connected to node : ",i+1
		e=int(raw_input())
		edge.append(e)
	graph.update({node:edge}) 
visited=[0]*len(graph)
queue=[]
def bfs(node):
        visited[node-1]=1
        queue.append(node)
        while(queue):
                print queue[0]
                x=queue.pop(0)
                for k in graph[x]:
                        if visited[k-1]==0:
                                queue.append(k)
                                visited[k-1]=1
print graph
start=time.clock()
bfs(1)
end=time.clock()
print "The program ran for ",(end-start)," seconds"
