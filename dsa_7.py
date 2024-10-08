# 2DMatries

# Q1. Column Sum
'''
Problem Description
You are given a 2D integer matrix A, return a 1D integer array containing column-wise sums of original matrix.

Problem Constraints
1 <= A.size() <= 103
1 <= A[i].size() <= 103
1 <= A[i][j] <= 103

Input Format
First argument is a 2D array of integers.(2D matrix).
Output Format
Return an array containing column-wise sums of original matrix.

Example Input
Input 1:
[1,2,3,4]
[5,6,7,8]
[9,2,3,4]

Example Output
Output 1:
{15,10,13,16}

Example Explanation
Explanation 1
Column 1 = 1+5+9 = 15
Column 2 = 2+6+2 = 10
Column 3 = 3+7+3 = 13
Column 4 = 4+8+4 = 16
'''

def columnSum(A):#Space complexity = O(M),    Time Complexity = O(C*R)>> O(M*N)
    C = len(A[0])
    R = len(A)
    arr = []
    for column in range(C):
        Sum = 0
        for row in range(R):
            Sum+=A[row][column]
        arr.append(Sum)
    return arr
'''
A = [[1,2,3,4],[5,6,7,8],[9,2,3,4]]
print(columnSum(A))
'''
# ------------------------------------------------------------------------------------------------------------------------------------------
# Q2. Main Diagonal Sum
'''
Problem Description
You are given a N X N integer matrix. You have to find the sum of all the main diagonal elements of A.
Main diagonal of a matrix A is a collection of elements A[i, j] such that i = j.

Problem Constraints
1 <= N <= 103
-1000 <= A[i][j] <= 1000

Input Format
There are 1 lines in the input. First 2 integers R, C are the number of rows and columns. Then R * C integers follow corresponding to the rowwise numbers in the 2D array A.
Output Format
Return an integer denoting the sum of main diagonal elements.

Example Input
Input 1:
3 3 1 -2 -3 -4 5 -6 -7 -8 9
Input 2:
2 2 3 2 2 3

Example Output
Output 1:
 15 
Output 2:
 6 

Example Explanation
Explanation 1:
The size of matrix is 3.
So, considering the indexing from 0.
Main diagonal elements will be A[0][0], A[1][1] and A[2][2]
A[1][1] + A[2][2] + A[3][3] = 1 + 5 + 9 = 15
Explanation 2:
The size of matrix is 2.
So, considering the indexing from 0.
Main diagonal elements will be A[0][0] and A[1][1].
A[1][1] + A[2][2] = 3 + 3 = 6
'''
def diagonalSum(A):#Space complexity = O(1),    Time Complexity = O(N)
    R = len(A)
    C = len(A[0])
    if R == C:
        i = 0; Sum = 0
        while(i<R):
            Sum+=A[i][i]
            i+=1
        return Sum
    else: print("Error!!")
'''
# A = [[1,-2,-3], [-4,5,-6], [-7,-8,9]]
A = [[3,2], [2,3]]
print(diagonalSum(A))
'''
# -----------------------------------------------------------------------------------------------------
# Q3. Anti Diagonals
'''
Problem Description
Give a N * N square matrix A, return an array of its anti-diagonals. Look at the example for more details.

Problem Constraints
1<= N <= 1000
1<= A[i][j] <= 1e9

Input Format
Only argument is a 2D array A of size N * N.
Output Format
Return a 2D integer array of size (2 * N-1) * N, representing the anti-diagonals of input array A.
The vacant spaces in the grid should be assigned to 0.

Example Input
Input 1:
1 2 3
4 5 6
7 8 9
Input 2:
1 2
3 4

Example Output
Output 1:
1 0 0
2 4 0
3 5 7
6 8 0
9 0 0
Output 2:
1 0
2 3
4 0

Example Explanation
For input 1:
The first anti diagonal of the matrix is [1 ], the rest spaces shoud be filled with 0 making the row as [1, 0, 0].
The second anti diagonal of the matrix is [2, 4 ], the rest spaces shoud be filled with 0 making the row as [2, 4, 0].
The third anti diagonal of the matrix is [3, 5, 7 ], the rest spaces shoud be filled with 0 making the row as [3, 5, 7].
The fourth anti diagonal of the matrix is [6, 8 ], the rest spaces shoud be filled with 0 making the row as [6, 8, 0].
The fifth anti diagonal of the matrix is [9 ], the rest spaces shoud be filled with 0 making the row as [9, 0, 0].
For input 2:
The first anti diagonal of the matrix is [1 ], the rest spaces shoud be filled with 0 making the row as [1, 0, 0].
The second anti diagonal of the matrix is [2, 4 ], the rest spaces shoud be filled with 0 making the row as [2, 4, 0].
The third anti diagonal of the matrix is [3, 0, 0 ], the rest spaces shoud be filled with 0 making the row as [3, 0, 0].
'''

def antidiagonals(A): #Space complexity = O(N^2),    Time Complexity = O(N^2 + N^2)>> N^2
    arr = [[0]*len(A) for i in range(2*len(A)-1)]
    for index in range(len(A)):
        row = 0; column = index; i = index; j = 0
        while(column>=0 and row < len(A)):
            arr[i][j] = A[row][column]
            row+=1; column-=1;j+=1
    for index in range(1,len(A)):
        row = index; column=len(A)-1;i=len(A)+(index-1); j = 0
        while (row<len(A) and column>=1):
            arr[i][j] = A[row][column]
            row+=1; column-=1; j+=1
    return arr
    '''
    p = len(A[0])
    res = [0]*(2*p-1)
    for i in range((2*p)-1):
        res[i] = []
    for i in range(p):
        for j in range(p):
            res[i+j].append(A[i][j])
    for i in range(2*p-1):
        while len(res[i]) < p:
            res[i].append(0)
    return res
    '''
'''
# A = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]
A = [[1,2],[3,4]]
print(antidiagonals(A))
'''
# ---------------------------------------------------------------------------------------------------------------
# Q4. Matrix Transpose
'''
Problem Description
Given a 2D integer array A, return the transpose of A.
The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

Problem Constraints
1 <= A.size() <= 1000
1 <= A[i].size() <= 1000
1 <= A[i][j] <= 1000

Input Format
First argument is a 2D matrix of integers.
Output Format
You have to return the Transpose of this 2D matrix.

Example Input
Input 1:
A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
Input 2:
A = [[1, 2],[1, 2],[1, 2]]

Example Output
Output 1:
[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
Output 2:
[[1, 1, 1], [2, 2, 2]]

Example Explanation
Explanation 1:
Clearly after converting rows to column and columns to rows of [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
 we will get [[1, 4, 7], [2, 5, 8], [3, 6, 9]].
Explanation 2:
After transposing the matrix, A becomes [[1, 1, 1], [2, 2, 2]]
'''

def transpose(A):#Space complexity = O(N*M),    Time Complexity = O(N*M)
    rows = len(A)
    columns = len(A[0])
    arr = [[0]*rows for i in range(columns)]
    for r in range(rows):
        for c in range(columns):
            arr[c][r]= A[r][c]
            print(arr[c][r])
    print(arr)
'''
A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
# A = [[1, 2],
# [1, 2],
# [1, 2]]
transpose(A)
'''
# ---------------------------------------------------------------------------------------------------------------------------------------
# Q5. Rotate Matrix

'''
Problem Description
You are given a n x n 2D matrix A representing an image.
Rotate the image by 90 degrees (clockwise).
You need to do this in place.
Note: If you end up using an additional array, you will only receive partial score.

Problem Constraints
1 <= n <= 1000

Input Format
First argument is a 2D matrix A of integers
Output Format
Return the 2D rotated matrix.

Example Input
Input 1:
 [  [1, 2],
    [3, 4]]
Input 2:
 [  [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9] ]

Example Output
Output 1:
 [  [3, 1],
    [4, 2]]
Output 2:
 [  [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3] ]

Example Explanation
Explanation 1:
 After rotating the matrix by 90 degree:
 1 goes to 2, 2 goes to 4
 4 goes to 3, 3 goes to 1
Explanation 2:
 After rotating the matrix by 90 degree:
 1 goes to 3, 3 goes to 9
 2 goes to 6, 6 goes to 8
 9 goes to 7, 7 goes to 1
 8 goes to 4, 4 goes to 2
 '''
def roatation(A): #Space complexity = O(1),    Time Complexity = O(N^2)
    N = len(A)
    for row in range(N):
        for column in range(row):
            temp = A[row][column]
            A[row][column] = A[column][row]
            A[column][row] = temp
    for index in range(N):
        i = 0; j=N-1
        while(i<j):
            temp = A[index][i]
            A[index][i] = A[index][j]
            A[index][j] = temp
            i+=1;j-=1
    return A
'''
# A =  [
#     [1, 2],
#     [3, 4]
#  ]
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
 ]
print(roatation(A))
'''
# -----------------------------------------------------------------------------------------
# Matrix Scalar Product
'''
Problem Description
You are given a matrix A and and an integer B, you have to perform scalar multiplication of matrix A with an integer B.

Problem Constraints
1 <= A.size() <= 1000
1 <= A[i].size() <= 1000
1 <= A[i][j] <= 1000
1 <= B <= 1000

Input Format
First argument is 2D array of integers A representing matrix.
Second argument is an integer B.
Output Format
You have to return a 2D array of integers after doing required operations.

Example Input
Input 1:
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
B = 2 
Input 2:
A = [[1]]
B = 5 

Example Output
Output 1:
[[2, 4, 6], 
[8, 10, 12], 
[14, 16, 18]]
Output 2:
[[5]]

Example Explanation
Explanation 1:
==> ( [[1, 2, 3],[4, 5, 6],[7, 8, 9]] ) * 2
==> [[2*1, 2*2, 2*3],
     [2*4, 2*5, 2*6],
     [2*7, 2*8, 2*9]]
==> [[2,   4,  6], 
     [8,  10, 12], 
     [14, 16, 18]]
Explanation 2:
==> ( [[1]] ) * 5
==> [[5*1]]
==> [[5]]
'''

def product(A,B):
    row = len(A)
    column = len(A[0])
    for r in range(row):
        for c in range(column):
            Sum = A[r][c]*B
            A[r][c] = Sum
    return A
'''
# A = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
# B = 2 
A = [[1]]
B = 5 
print(product(A,B))
'''
# -------------------------------------------------------------------------------------------------------------------------------------------
# Q2. Add the matrices

'''
Problem Description

You are given two matrices A & B of same size, you have to return another matrix which is the sum of A and B.
Note: Matrices are of same size means the number of rows and number of columns of both matrices are equal.
The Following will give you an idea of matrix addition:

Problem Constraints
1 <= A.size(), B.size() <= 1000 1 <= A[i].size(), B[i].size() <= 1000 1 <= A[i][j], B[i][j] <= 1000
Input Format
The first argument is the 2D integer array A The second argument is the 2D integer array B
Output Format
You have to return a vector of vector of integers after doing required operations.
Example Input

Input 1:
A = [[1, 2, 3],   
     [4, 5, 6],   
     [7, 8, 9]]  
B = [[9, 8, 7],   
     [6, 5, 4],   
     [3, 2, 1]]
 
Input 2:
A = [[1, 2, 3],   
     [4, 1, 2],   
     [7, 8, 9]]  
B = [[9, 9, 7],   
     [1, 2, 4],   
     [4, 6, 3]]
 
Example Output
Output 1:
[[10, 10, 10],   
 [10, 10, 10],   
 [10, 10, 10]]
Output 2:
[[10, 11, 10],   
 [5,   3,  6],   
 [11, 14, 12]]
Example Explanation
Explanation 1:
A + B = [[1+9, 2+8, 3+7],  
         [4+6, 5+5, 6+4],  
         [7+3, 8+2, 9+1]]   
      = [[10, 10, 10],   
         [10, 10, 10],   
         [10, 10, 10]].
Explanation 2:
A + B = [[1+9, 2+9, 3+7],  
         [4+1, 1+2, 2+4],  
         [7+4, 8+6, 9+3]]   
      = [[10, 11, 10],   
         [5,   3,  6],   
         [11, 14, 12]].
'''


def addition(A,B):
    row = len(A)
    column = len(A[0])
    arr = []
    for index in range(row):
        arr.append([])
    for r in range(row):
        for c in range(column):
            Sum = A[r][c] + B[r][c]
            arr[r].append(Sum)
    return arr
'''
A = [[1, 2, 3],   
     [4, 5, 6],   
     [7, 8, 9]]  

B = [[9, 8, 7],   
     [6, 5, 4],   
     [3, 2, 1]]

A = [[1, 2, 3],   
     [4, 1, 2],   
     [7, 8, 9]]  

B = [[9, 9, 7],   
     [1, 2, 4],   
     [4, 6, 3]]
print(addition(A,B))
'''
# -------------------------------------------------------------------------------------------------------------------------------------
# Q3. Minor Diagonal Sum

'''
Problem Description
You are given a N X N integer matrix. You have to find the sum of all the minor diagonal elements of A.
Minor diagonal of a M X M matrix A is a collection of elements A[i, j] such that i + j = M + 1 (where i, j are 1-based).

Problem Constraints
1 <= N <= 103
-1000 <= A[i][j] <= 1000

Input Format
First and only argument is a 2D integer matrix A.
Output Format
Return an integer denoting the sum of minor diagonal elements.

Example Input
Input 1:
 A = [[1, -2, -3],
      [-4, 5, -6],
      [-7, -8, 9]]
Input 2:
 A = [[3, 2],
      [2, 3]]

Example Output
Output 1:
-5 
Output 2:
4 
Example Explanation
Explanation 1:
 A[1][3] + A[2][2] + A[3][1] = (-3) + 5 + (-7) = -5
Explanation 2:
 A[1][2] + A[2][1] = 2 + 2 = 4
'''

def minor_diagonal_sum(A):
    Sum =0; i =0 ; j= len(A)-1
    while(i<len(A)):
        Sum += A[i][j]
        i+=1;j-=1
    return Sum
'''
# A = [[1, -2, -3],
#       [-4, 5, -6],
#       [-7, -8, 9]]
A = [[3, 2],
      [2, 3]]
print(minor_diagonal_sum(A))
'''
# -----------------------------------------------------------------------------------------------------------------------
# Q4. Row Sum
'''
Problem Constraints
1 <= A.size() <= 103
1 <= A[i].size() <= 103
1 <= A[i][j] <= 103

Input Format
First argument A is a 2D array of integers.(2D matrix).

Output Format
Return an array containing row-wise sums of original matrix.
Example Input
Input 1:
[1,2,3,4]
[5,6,7,8]
[9,2,3,4]

Example Output
Output 1:
[10,26,18]

Example Explanation
Explanation 1
Row 1 = 1+2+3+4 = 10
Row 2 = 5+6+7+8 = 26
Row 3 = 9+2+3+4 = 18
'''
def rowSum(A):
    row = len(A)
    column = len(A[0])
    arr = []
    for r in range(row):
        row_sum = 0
        for c in range(column):
            row_sum += A[r][c]
        arr.append(row_sum)
    return arr
'''
A = [[1,2,3,4],
[5,6,7,8],
[9,2,3,4]]
print(rowSum(A))
'''

arr = [[0]*5 for index in range(5)]





    



