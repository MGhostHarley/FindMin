
import time 
from random import randrange

def find_min_On2(aList): #the point of this function is to find the minmumum. It uses nested for loops to compare on element in the list to everey other element and do that over and over until it finds the smallest

	is_smallest = aList[0]

	for counter1 in xrange(len(aList)):
		for counter2 in xrange(len(aList)):
			if aList[counter1] > aList[counter2]:
				is_smallest = aList[counter2]

	return is_smallest




def find_min_linear(alist): #the point of this function is to find the minmumum. This function takes the first element and compares to the next; which ever is smallest is then saved and compared to the next element to the smallest is found

	min_so_far = alist[0]

	for counter in xrange(len(alist)):
		if alist[counter] < min_so_far:
			min_so_far = alist[counter]

	return min_so_far


#example_list = [6,2,4,7,8,3]
#print find_min_linear(example_list)
#print find_min_On2(example_list)

def main():

#This first for loop tests the speed of the linear function
	print "\nThis is the linear time testing\n"
	for listSize1 in range(1000,10001,1000): # starts off with lists of a thousand, goes up to 10,000 and grows each list by a thousand
		alist1 = [randrange(100000) for x in range (listSize1)] #list comprehension that states populate a list between 0 and 100,000 for the range of list size
		start1 = time.time()
		print find_min_linear(alist1)
		end1 = time.time()
		print "Size: %d time %f " %(listSize1, end1-start1)

#This second for loop tests the speed of the quadratic function
	print "\nThis is the n^2 time testing\n"	
	for listSize in range(1000,10001,1000):
		alist = [randrange(100000) for x in range (listSize)]
		start = time.time()
		print find_min_On2(alist)
		end = time.time()
		print "Size: %d time %f " %(listSize, end-start)

main()