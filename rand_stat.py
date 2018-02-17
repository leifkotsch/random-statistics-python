from random import randint
import sys

iters = int(sys.argv[1]) # argument iterations
maxa = int(sys.argv[2]) # argument max

all = []
stat = []

def main(iter,min,max):
	for temp in range(min,max + 1): # +1 because index is 0
		stat.append(0)
	old_randint = -1
	double_same = 0
	for i in range(iter):
		rint = randint(min,max)
		#all.append(rint)
		if(old_randint == rint):
			double_same += 1
		old_randint = rint
		old_count = stat[rint]
		stat[rint] = old_count + 1
	co = 0
	print("Statistics for {} iterations through random numbers from {} to {}:\r\n".format(iter,min,max))
	for _ in stat:
		print("{} apeared {} times.".format(co,_))
		co += 1
	print("\r\n{} same random numbers apeared successively.".format(double_same))
	#print(all)

main(int(iters),0,maxa)
