# a program to define a array 3x3 and , 
# randomly assigns values between 0 to 20
# then , perform(anjam dadan) the following action ==>
# display the sum of the matrix elements 
# display the avarage of sum of matrix elements 
# display the largest element of each row 
# display the smallest element of each column 
import numpy as np 
import random 
import numpy.matlib  
def create_random(arr,n,m) :
    for i in range(0,n) :
        for j in range(0,m):
            arr[i,j] = random.randint(0,20)
    return arr
def print_array(arr,n,m):
    for i in range(0,n):
        for j in range(0,m) :
            print(arr[i,j],end=" \t")
        print()
def main() : 
    n= m = 3 
    a = np.matlib.empty((n,m),dtype = 'i')
    a = create_random(a,n,m)
    print_array(a,n,m)
    print("=======================")
    print("sum is ",np.sum(a))
    print("average is ",np.average(a))
    print(" max rows are => ",np.amax(a,axis =1))
    print("min columns are ",np.amin(a,axis = 0))
main()
# in main function ==> 
    # n = number of rows of array 
    # m = number of columns of array 
    # a = aray 3x3 
# in create_random or print_array function ==>
    # arr = an array that should full with random number between 0 to 20 or print
    # n = number of rows
    # m = number of columns
    # i = counter of rows from 0 to n-1
    