
# coding: utf-8

# Thomas Carter <br>
# 10/10/2020

# This program uses dynamic programming in python to find the most cost effective way to multiply a chain of matrices.

# In[3]:


#Imports

import sys
import random


# Function

def MatrixChainOrder(p, n):
    # For simplicity of the program, one extra row and one 
    # extra column are allocated in m[][].  0th row and 0th 
    # column of m[][] are not used 
    m = [[0 for x in range(n)] for x in range(n)] 
    
    # m[i,j] = Minimum number of scalar multiplications needed 
    # to compute the matrix A[i]A[i+1]...A[j] = A[i..j] where 
    # dimension of A[i] is p[i-1] x p[i] 
    
    # cost is zero when multiplying one matrix. 
    for i in range(1, n): 
        m[i][i] = 0
  
    # L is chain length. 
    for L in range(2, n): 
        for i in range(1, n-L+1): 
            j = i+L-1
            m[i][j] = sys.maxsize 
            for k in range(i, j): 
  
                # q = cost/scalar multiplications 
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j] 
                if q < m[i][j]: 
                    m[i][j] = q 
  
    return m[1][n-1] 


# Main

print("Please write the number of matrices to multiply: ")
n = int(input())

#This array stores the dimensions of the matrices that will be multiplied. 
#For example, matrix i will be of size p[i-1] x p[i]
arr = []

print("Would you like to auto-fill the matrices' dimensions with random numbers? [Y] Or would you like to manually fill the dimensions? [N]")
ans = input()

if ans == "Y":
    for i in range(n+1):
        r = random.randint(1,100)
        
        arr.append(r)
        
elif ans == "N":
    print("Line up the matrices dimensions in the way they can be multiplied (Example: for the matrices 10x5 and 5x20 you should write 10 then 5 then 20 in the input))")
    for t in range(n+1):
        print("Dimension", t+1, ":")
        r = int(input())
        arr.append(r)

print("Dimensions of the matrices: " + str(arr))

print("Minimum number of multiplications is " + str(MatrixChainOrder(arr, (n+1)))) 

