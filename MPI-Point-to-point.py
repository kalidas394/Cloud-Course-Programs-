#! usr/bin/env python

from mpi4py import MPI as mpi
import numpy as np
import scipy as sp
import time

a = np.arange(0,10000,0.01).reshape((1000,1000))

b = np.transpose(a)

dotp = np.dot(a,b)
#print "Actual Dot product value is:", dotp

comm = mpi.COMM_WORLD
rank = comm.Get_rank()

def blockshaped(arr, nrows, ncols):
    """
    Return an array of shape (n, nrows, ncols) where
    n * nrows * ncols = arr.size

    If arr is a 2D array, the returned array should look like n subblocks with
    each subblock preserving the "physical" layout of arr.
    """
    h, w = arr.shape
    return (arr.reshape(h//nrows, nrows, -1, ncols)
               .swapaxes(1,2)
               .reshape(-1, nrows, ncols))

c = blockshaped(a,100, 1000)

g = 0
h = 0
d = range(0,1000000, 100000)
if (rank == 0):
                 for i in c:
                          g = g+1
                          comm.Send(i, dest=g, tag = 10)
                          
                 for j in d:
                         
                          h = h+1
                          comm.Send(b, dest=h, tag = 11)
                 m = np.empty(100000, np.float64).reshape((100,1000))
                 comm.Recv(m , source = 1, tag = 12)
                 time.sleep(0.5)

      		 mone = np.empty(100000, np.float64).reshape((100,1000))
                 comm.Recv(mone , source = 2, tag = 13)
                 time.sleep(0.5)
		
		 mtwo = np.empty(100000, np.float64).reshape((100,1000))
                 comm.Recv(mtwo , source = 3, tag = 14)
                 time.sleep(0.5)

 		 mthree = np.empty(100000, np.float64).reshape((100,1000))
                 comm.Recv(mthree , source = 4, tag = 15)
                 time.sleep(0.5)

		 mfour = np.empty(100000, np.float64).reshape((100,1000))
                 comm.Recv(mfour , source = 5, tag = 16)
                 time.sleep(0.5)
		
		 mfive = np.empty(100000, np.float64).reshape((100,1000))
                 comm.Recv(mfive , source = 6, tag = 17)
                 time.sleep(0.5)

		 msix = np.empty(100000, np.float64).reshape((100,1000))
                 comm.Recv(msix , source = 7, tag = 18)
                 time.sleep(0.5)
 
    	         mseven = np.empty(100000, np.float64).reshape((100,1000))
                 comm.Recv(mseven , source = 8, tag = 19)
                 time.sleep(0.5)
		  
		 meight = np.empty(100000, np.float64).reshape((100,1000))
                 comm.Recv(meight , source = 9, tag = 20)
                 time.sleep(0.5)
		 
		 mnine = np.empty(100000, np.float64).reshape((100,1000))
                 comm.Recv(mnine , source = 10, tag = 21)
                 time.sleep(0.5)
                
 		 nonee = np.concatenate((m, mone, mtwo, mthree, mfour, mfive, msix, mseven, meight, mnine), axis = 0)
                 
                 print "The final matrix is:\n", nonee
                 assert dotp.all() == nonee.all()
                 

elif rank == 1:
        i = np.empty(100000, np.float64).reshape((100,1000))
        j = np.empty(1000000, np.float64).reshape((1000,1000))
        comm.Recv(i, source=0, tag = 10)
        comm.Recv(j, source=0, tag = 11)
        print "I am slave %d\n"%rank
        n = np.empty(100000, np.float64).reshape((100,1000))
        p = np.transpose(j)
        n = np.dot(i,p)
        print "\n", n
        comm.Send(n, dest = 0, tag = 12)
elif rank == 2:
        i = np.empty(100000, np.float64).reshape((100,1000))
        j = np.empty(1000000, np.float64).reshape((1000,1000))
        comm.Recv(i, source=0, tag = 10)
        comm.Recv(j, source=0, tag = 11)
        print "I am slave %d\n"%rank
        n = np.empty(100000, np.float64).reshape((100,1000))
        p = np.transpose(j)
        n = np.dot(i,p)
        print "\n", n
        comm.Send(n, dest = 0, tag = 13)

elif rank == 3:
        i = np.empty(100000, np.float64).reshape((100,1000))
        j = np.empty(1000000, np.float64).reshape((1000,1000))
        comm.Recv(i, source=0, tag = 10)
        comm.Recv(j, source=0, tag = 11)
        print "I am slave %d\n"%rank
        n = np.empty(100000, np.float64).reshape((100,1000))
        p = np.transpose(j)
        n = np.dot(i,p)
        print "\n", n
        comm.Send(n, dest = 0, tag = 14)

elif rank == 4:
        i = np.empty(100000, np.float64).reshape((100,1000))
        j = np.empty(1000000, np.float64).reshape((1000,1000))
        comm.Recv(i, source=0, tag = 10)
        comm.Recv(j, source=0, tag = 11)
        print "I am slave %d\n"% rank
        n = np.empty(100000, np.float64).reshape((100,1000))
        p = np.transpose(j)
        n = np.dot(i,p)
        print "\n",n
        comm.Send(n, dest = 0, tag = 15)

elif rank == 5:
        i = np.empty(100000, np.float64).reshape((100,1000))
        j = np.empty(1000000, np.float64).reshape((1000,1000))
        comm.Recv(i, source=0, tag = 10)
        comm.Recv(j, source=0, tag = 11)
        print "I am slave %d\n" % rank
        n = np.empty(100000, np.float64).reshape((100,1000))
        p = np.transpose(j)
        n = np.dot(i,p)
        print "\n", n
        comm.Send(n, dest = 0, tag = 16)

elif rank == 6:
        i = np.empty(100000, np.float64).reshape((100,1000))
        j = np.empty(1000000, np.float64).reshape((1000,1000))
        comm.Recv(i, source=0, tag = 10)
        comm.Recv(j, source=0, tag = 11)
        print "I am slave %d\n" % rank
        n = np.empty(100000, np.float64).reshape((100,1000))
	p = np.transpose(j)
        n = np.dot(i,p)
        print "\n", n
        comm.Send(n, dest = 0, tag = 17)

elif rank == 7:
        i = np.empty(100000, np.float64).reshape((100,1000))
        j = np.empty(1000000, np.float64).reshape((1000,1000))
        comm.Recv(i, source=0, tag = 10)
        comm.Recv(j, source=0, tag = 11)
        print "I am slave %d\n"%rank
        n = np.empty(100000, np.float64).reshape((100,1000))
	p = np.transpose(j)
        n = np.dot(i,p)
        print "\n", n
        comm.Send(n, dest = 0, tag = 18)

elif rank == 8:
        i = np.empty(100000, np.float64).reshape((100,1000))
        j = np.empty(1000000, np.float64).reshape((1000,1000))
        comm.Recv(i, source=0, tag = 10)
        comm.Recv(j, source=0, tag = 11)
        print "I am slave %d\n"%rank
        n = np.empty(100000, np.float64).reshape((100,1000))
   	p = np.transpose(j)
        n = np.dot(i,p)
        print "\n", n
        comm.Send(n, dest = 0, tag = 19)

elif rank == 9:
        i = np.empty(100000, np.float64).reshape((100,1000))
        j = np.empty(1000000, np.float64).reshape((1000,1000))
        comm.Recv(i, source=0, tag = 10)
        comm.Recv(j, source=0, tag = 11)
        print "I am slave %d\n"%rank
        n = np.empty(100000, np.float64).reshape((100,1000))
  	p = np.transpose(j)
        n = np.dot(i,p)
        print "\n", n
        comm.Send(n, dest = 0, tag = 20)

elif rank == 10:
        i = np.empty(100000, np.float64).reshape((100,1000))
        j = np.empty(1000000, np.float64).reshape((1000,1000))
        comm.Recv(i, source=0, tag = 10)
        comm.Recv(j, source=0, tag = 11)
        print "I am slave %d\n"%rank
        n = np.empty(100000, np.float64).reshape((100,1000))
 	p = np.transpose(j)
        n = np.dot(i,p)
        print "\n", n
        comm.Send(n, dest = 0, tag = 21)
