# a program to read a prime number (adad aval)
# and get in output :all prime number before of that number with using the function 
# ADADI PRIME AST KE : BAR HICH ADAD AVAL GHABL AZ KHOD GHABEL GHESMAT NBASHAD 
from array import *
def prime(a,tedad,num) : 
    for i in range(0,tedad) : 
        if num % a[i] == 0 :
            return 0 
    a.append(num)
    return 1 
def main():
    tedad = 0 
    p = array('i',[]) 
    n = int(input("enter number ==> "))
    for i in range(2,n+1):
        if prime(p,tedad,i) == 1 :
            tedad = tedad + 1 
    print("primary is ",end=" ")
    for i in range(0,tedad) :
        print(" ",p[i],end=" ")
main()
# PRIME METHOD ==>
# TASHKHIS MIDAHAD ADADI PRIME AST OR NO ? 
# IF PRIME BASHAD , 1 RA RETURN MIKONAD .
###############################################
# IN METHOD MAIN =>
# n = READED NUMBER (ADAD KHANDE SHODE) 
# P = ARAYEI AZ AADAD PRIME 
# i = counter 
# TEDAD = NUMBER OF PRIME NUMBER 
#####################################
# IN METHOD PRIME ==> 
# i = counter 