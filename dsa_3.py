# def rotate(li, N, K): #brute force approch   >>>>>>> time complexity 
#     for i in range(K):   # >> iterate's K times >> K
#         temp = li[N-1]
#         for j in range(N-1,0,-1):  # >> iretate's [1,N-1] >> N-1-1+1 >> N-1 times
#             li[j]= li[j-1]
#         li[0]=temp
#     return li              # >> Therefore  K * N-1 >> KN - K >>> O(KN) times====      Space Complexity= Thee is no extra space required, hence O(1)   

# li = [1,2,3,4,5]
# N  = len(li)
# print(rotate(li,len(li),5))

# ====================================================================================================
# above code with optimization

def reverse(li,s,e):    #Space complexity = O(1),     Time complexity = O(N)
    i, j = s, e
    while i<j:
        temp = li[i]
        li[i] = li[j]
        li[j] = temp
        i+=1; j-=1
    return li

def rotate1(li,N,K):   #Space complexity = O(1),     Time complexity = O(N)
    if K>N:
        K=K%N
    reverse(li,0,N-1)
    reverse(li,0,K-1)
    reverse(li,K,N-1)
    return li
li = [1,2,3,4]
N = len(li)
print(rotate1(li,N,6))

# -------------------------------------------------------------------------------------------------------------------
# Given an array A and an integer B. A pair(i, j) in the array is a good pair if i != j and (A[i] + A[j] == B). Check if any good pair exist or not.

# Problem Constraints
# 1 <= A.size() <= 104 >> 10^6  
# 1 <= A[i] <= 109  >> 10^6
# 1 <= B <= 109 >> 10^6



# def good_pair(a,b):   #Space complexity = O(1),  Time complexity = O(n^2)
#     good_pair = 0
#     for index_i, ele in enumerate(a):
#         for index_j in range(index_i+1,len(a)):
#             if (ele + a[index_j]) == b:
#                 good_pair+=1
#             else: pass
#     if good_pair > 0:
#         return 1
#     else: return 0

# a = [1,2,1]
# print(good_pair(a,4))

# ---------------------------------------------------------------------------------------------------------------------------------------------


# Given an array A of N integers and also given two integers B and C. Reverse the elements of the array A within the given inclusive range [B, C].
    # Problem Constraints
    # 1 <= N <= 105
    # 1 <= A[i] <= 109
    # 0 <= B <= C <= N - 1


# Input Format
# The first argument A is an array of integer.
# The second and third arguments are integers B and C


# Output Format
# Return the array A after reversing in the given range.


'''
A = [2, 5, 6]
B = 0
C = 2
print(reverse(A,B,C))'''

# ---------------------------------------------------------------------------------------------------------------------------------

# Given an array A of size N. You need to find the sum of Maximum and Minimum element in the given array.

    # Problem Constraints
    # 1 <= N <= 105
    # -109 <= A[i] <= 109

# Input Format
# First argument A is an integer array.


# Output Format
# Return the sum of maximum and minimum element of the array

'''
def Sum_max_min(A):   #Space complexity = O(1),    Time Complexity = O(N)
    Max = Min = A[0]
    for item in A:
        if item >= Max:
            Max = item
        if item <= Min:
            Min = item
    return Min+Max
A = [1, 3, 4, 1]
print(Sum_max_min(A))

'''
# -----------------------------------------------------------------------------------------------------------------------------------
# Problem Description
# Given an array A and an integer B, find the number of occurrences of B in A.

    # Problem Constraints
    # 1 <= B, Ai <= 109
    # 1 <= length(A) <= 105

# Input Format
# Given an integer array A and an integer B.


# Output Format
# Return an integer, number of occurrences of B in A.

'''
def occurrences(A,B):   #Space complexity = O(1),    Time Complexity = O(N)
    Count = 0
    for item in A:
        if item == B:
            Count+=1
        else: pass
    return Count

A = [1, 2, 1]; B = 3 
print(occurrences(A,B))
'''

# ------------------------------------------------------------------------------------------------------------------------------

# Problem Description
# Given an array A of N integers. 
# Count the number of elements that have at least 1 elements greater than itself.

    # Problem Constraints
    # 1 <= N <= 105
    # 1 <= A[i] <= 109

# Input Format
# First and only argument is an array of integers A.


# Output Format
# Return the count of elements.

'''
def greater_check(A):    #Wrong ---------------- need to check--------------------------
    Count=0
    Max = max(A)
    for i in range(len(A)-1):
        if 
            Count+=1
    return Count
A = [5, 5, 1,3,4]
print(greater_check(A))
'''

# ----------------------------------------------------------------------------------------------------------------------------------

# Problem Description
# You are given an integer array A. You have to find the second largest element/value in the array or report that no such element exists.

    # Problem Constraints
    # 1 <= |A| <= 105
    # 0 <= A[i] <= 109

# Input Format
# The first argument is an integer array A.

# Output Format
# Return the second largest element. If no such element exist then return -1.

'''
def second_largest(A):
    Max = A[0]; Smax = -1
    A = set(A)
    A = list(A)
    for i in range(1,len(A)):
        if A[i]>Max:
            Smax = Max
            Max = A[i]
        else: Smax = A[i]
    return Smax

A = [2,1,0,1,10,50,1,100,200,0]
print(second_largest(A))
'''









