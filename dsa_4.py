###########################################################################################################################################
# Prefix_sum:->    Prefix sum is the technique where you precompute & store the cumulative sum of the sequence of elements that allows fast
#                  sum calculation of any continuous range.

 
'''
Let's say we have a sequence of elements A as mentioned below-
A = {a0, a1, a2, a3, a4, a5}
so Prefix Sum P will be calculated as
P=  {p0, p1, p2, p3, p4, p5}
where-
p0 = a0
p1 = a1 + a0
p2 = a0 + a1 + a2
p3 = a0 + a1 + a2 + a3 
p4 = a0 + a1 + a2 + a3 + a4
p5 = a0 + a1 + a2 + a3 + a4 + a5
Q) Say we need to sum get sum of all elements from indices 
 [2 to 5] => [a2 + a3 + a4 + a5]  or [p5 - p1] 
 [1 to 4] => [a1 + a2 + a3 + a4]      or [p4 - p0]
 [0 to 4] => [a0 + a1 + a2 + a3 + a4]  or  [p4]
 '''

###########################################################################################################################################
# Q3. Range Sum Query

# Problem Description
# You are given an integer array A of length N.
# You are also given a 2D integer array B with dimensions M x 2, where each row denotes a [L, R] query.
# For each query, you have to find the sum of all elements from L to R indices in A (0 - indexed).
# More formally, find A[L] + A[L + 1] + A[L + 2] +... + A[R - 1] + A[R] for each query.

    # Problem Constraints
    # 1 <= N, M <= 105
    # 1 <= A[i] <= 109
    # 0 <= L <= R < N

# Input Format
# The first argument is the integer array A.
# The second argument is the 2D integer array B.

# Output Format
# Return an integer array of length M where ith element is the answer for ith query in B.


def Range_Sum(A,B): #Brutfource Approch..............    #Space complexity = O(N),    Time Complexity = O(N^2 or MN) So, based on the constraint if M = 10^5 AND N = 10^5 ==> 10^10 which is TLE
    arr = []
    for index in range(len(B)):
        L,R = B[index][0], B[index][1]
        Sum = 0
        for index_1 in range(L,R+1):
            Sum+=A[index_1]
        arr.append(Sum)
    return arr

def Range_Sum1(A,B):  #Optimized Approch...................   #Space complexity = O(M+N),    Time Complexity = O(A+B or M+N) >> So, based on the constraint if M = 10^5 AND N = 10^5 ==> 10^5+10^5 which is not TLE
    def pre_fix(A):   # Pre-Fix method    
        arr = []
        arr.append(A[0])
        for index in range(1, len(A)):
            pre_fix = arr[index-1]
            Sum = pre_fix + A[index]
            arr.append(Sum)
        return arr


    A = pre_fix(A)
    arr = []
    for index in range(len(B)):
        L,R,Sum = B[index][0], B[index][1], 0
        if L > 0:
            Sum = A[R] - A[L-1]
            arr.append(Sum)
        else: arr.append(A[R])
    return arr
        

# A = [1, 2, 3, 4, 5]
# B = [[0, 3], [1, 2]]
'''
A = [2, 2, 2]
B = [[0, 0], [1, 2]]
print(Range_Sum(A,B))
print(Range_Sum1(A,B))
'''

# --------------------------------------------------------------------------------------------------------------------------------------------

# Q4. Special Index

# Problem Description
# Given an array, arr[] of size N, the task is to find the count of array indices such that removing an element from these indices makes the 
# sum of even-indexed and odd-indexed array elements equal.

    # Problem Constraints
    # 1 <= N <= 105
    # -105 <= A[i] <= 105
    # Sum of all elements of A <= 109

# Input Format
# First argument contains an array A of integers of size N

# Output Format
# Return the count of array indices such that removing an element from these indices makes the sum of even-indexed and odd-indexed array elements 
# equal.


def prefix_EorO(A,Value):
    arr = []
    if Value.upper() == "EVEN":
        arr.append(A[0])
        for index in range(1,len(A)):
            if index%2 != 0:
                Sum = arr[index-1]
                arr.append(Sum)
            else: 
                Sum = arr[index-1]+A[index]
                arr.append(Sum)
        return arr

    elif Value.upper() == "ODD":
        arr.append(0)
        for index in range(1,len(A)):
            if index%2 == 0:
                Sum = arr[index-1]
                arr.append(Sum)
            else: 
                Sum = arr[index-1]+A[index]
                arr.append(Sum)
        return arr
    else:
        print("Please enter the correct value(EVEN/ODD)")

def Special_Index(A):
    P_O = prefix_EorO(A,"odd")
    P_E = prefix_EorO(A,"Even")
    Count = 0
    for index in range(len(A)):
        if index > 0:
            S_E = P_E[index-1] + (P_O[len(P_O)-1] - P_O[index])
            S_O = P_O[index-1] + (P_E[len(P_O)-1] - P_E[index])
        else:
            S_E = P_O[len(P_O)-1] - P_O[index]
            S_O = P_E[len(P_E)-1] - P_E[index]

        if S_E == S_O:
            Count+=1
    return Count
        

'''
# A = [2, 1, 6, 4]
A = [1, 1, 1]
print(Special_Index(A))
'''




# ------------------------------------------------------------------------------------------------------------------------------------------------

# Q7. In-place Prefix Sum

# Problem Description
# Given an array A of N integers. Construct prefix sum of the array in the given array itself.

    # Problem Constraints
    # 1 <= N <= 105
    # 1 <= A[i] <= 103

# Input Format
# Only argument A is an array of integers.

# Output Format
# Return an array of "integers" denoting the prefix sum of the given array.

A = "integers"
A1 = [1,2,4,5]
print(type(A))
for item in A:
    print(item)



def pre_fix_same_array(A):
    for index in range(1,len(A)):
        A[index] = A[index-1] + A[index]
    return A

'''
# A = [1, 2, 3, 4, 5]
A = [4, 3, 2]
print(pre_fix_same_array(A))

'''

# --------------------------------------------------------------------------------------------------------------------------------------------
# Q2. Equilibrium index of an array

# Problem Description
# You are given an array A of integers of size N.
# Your task is to find the equilibrium index of the given array
# The equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.
# If there are no elements that are at lower indexes or at higher indexes, then the corresponding sum of elements is considered as 0.

# Note:
# Array indexing starts from 0.
# If there is no equilibrium index then return -1.
# If there are more than one equilibrium indexes then return the minimum index.

    # Problem Constraints
    # 1 <= N <= 105
    # -105 <= A[i] <= 105

# Input Format
# First arugment is an array A .

# Output Format
# Return the equilibrium index of the given array. If no such index is found then return -1.

def pre_fix1(A):
    arr = []
    arr.append(A[0])
    for index in range(1,len(A)):
        Sum = arr[index-1] + A[index]
        arr.append(Sum)
    return arr

def equilibrium(A):
    A = pre_fix1(A)
    e_q = -1
    for index in range(len(A)):
        if index > 0 and index < len(A)-1:
            Sum_L = A[index-1]
            R_L = A[index]
            R_R = A[len(A)-1]
            Sum_R = R_R - R_L
            if Sum_L == Sum_R:
                e_q = index
    return e_q

'''
# A = [-7,1,5,2,-4,3,0]
A = [-5,1,2,3,4,8,10,-5]

print(equilibrium(A))
print(pre_fix1(A))

'''




# ---------------------------------------------------------------------------------------------------------------------------------------------

# Q3. In-place Prefix Sum

# Problem Description
# Given an array A of N integers. Construct prefix sum of the array in the given array itself.

    # Problem Constraints
    # 1 <= N <= 105
    # 1 <= A[i] <= 103

# Input Format
# Only argument A is an array of integers.

# Output Format
# Return an array of integers denoting the prefix sum of the given array.

'''
# A = [1, 2, 3, 4, 5]
A = [4, 3, 2]
print(pre_fix_same_array(A))

'''


# ----------------------------------------------------------------------------------------------------------------------------------------------