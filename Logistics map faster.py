import matplotlib.pyplot as plt
#import time

#start = time.time()

n = 0.01
r = 2.0                    #where the graph starts

steps = 10000000
k = 0.0000002                 #the smaller k is the closer the points are

xs = [r+k*i for i in range(steps)]
ys = [0 for _ in range(steps)]

print k*steps+r                 #equals end of graph (want it to be 4.0)

for index, x in enumerate(xs):
    a = x*n*(1-n)
    ys[index] = a
    n = a

#print "Time taken: %.2f" %(time.time()-start)

plt.xlabel("r")
plt.ylabel("x")

plt.scatter(xs,ys,s=0.01)     #'s' is the size of each point
plt.show()
