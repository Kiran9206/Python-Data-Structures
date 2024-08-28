# Q2. Closest MinMax

# Problem Description
# Given an array A, find the size of the smallest subarray such that it contains at least one occurrence of the maximum value of the array
# and at least one occurrence of the minimum value of the array.

    # Problem Constraints
    # 1 <= |A| <= 2000

# Input Format
# First and only argument is vector A

# Output Format
# Return the length of the smallest subarray which has at least one occurrence of minimum and maximum element of the array

def min_max(A):
    Min = Max = A[0]
    for item in A:
        if Min > item:
            Min = item
        elif Max < item:
            Max = item
    return Min, Max

def mm_subarray(A):  #Brute force approach........  #Space complexity = O(1),    Time Complexity = O(N(2N)) ?? 2N+N^2 >>> O(N^2)
    Min = min_max(A)[0]
    Max = min_max(A)[1]
    length = 10**9
    for index, item in enumerate(A):
        if item == Min:
            for index_1 in range(index+1,len(A)):
                if A[index_1] == Max:
                    length = min(length,(index_1-index)+1)
                    break
        elif item == Max:
             for index_1 in range(index+1,len(A)):
                if A[index_1] == Min:
                    length = min(length,(index_1-index)+1)
                    break
    return length


def mm_subarray_optimization(A): # Carry-forward technique............#Space complexity = O(1),    Time Complexity = O(N)
    Min = min_max(A)[0]
    Max = min_max(A)[1]
    min_i=max_i=-1; ans = 10**9
    for index, item in enumerate(A):
        if Min == item:
            min_i = index
            if max_i != -1:
                ans = min(ans,abs(min_i-max_i)+1)
        elif Max == item:
            max_i = index
            if min_i != -1:
                ans = min(ans,abs(max_i-min_i)+1)
    return ans
        


    
'''
A = [2, 6, 1, 6, 9]
# A = [1, 3, 2]
# A = [1,2,3,1,1,3,4,6,4,6,3]
# A = [2,2,6,4,5,1,5,2,6,4,1]
print(mm_subarray_optimization(A))
'''





# ----------------------------------------------------------------------------------------------------------------------------------

# Q4. Subarray in given range

# Problem Description
# Given an array A of length N, return the subarray from B to C.

    # Problem Constraints
    # 1 <= N <= 105
    # 1 <= A[i] <= 109
    # 0 <= B <= C < N

# Input Format
# The first argument A is an array of integers
# The remaining argument B and C are integers.

# Output Format
# Return a subarray

def subarray(A,B,C):  #Space complexity = O(N),    Time Complexity = O(N)
    arr = []
    for index in range(B,C+1):
        arr.append(A[index])
    return arr

'''
# A = [4, 3, 2, 6]
# B = 1
# C = 3

A = [4, 2, 2]
B = 0
C = 1

print(subarray(A,B,C))

'''


# -----------------------------------------------------------------------------------------------------------------------------------

# Q5. Generate all subarrays

# Problem Description
# You are given an array A of N integers.
# Return a 2D array consisting of all the subarrays of the array
# Note : The order of the subarrays in the resulting 2D array does not matter.

    # Problem Constraints
    # 1 <= N <= 100
    # 1 <= A[i] <= 105

# Input Format
# First argument A is an array of integers.

# Output Format
# Return a 2D array of integers in any order.

def all_subarray(A):   #Brute force approach........  #Space complexity = O(N^2),    Time Complexity = O(n^3)
    arr = []
    for index in range(len(A)):
        for index_1 in range(index,len(A)):
            arr1 = []
            for index_2 in range(index,index_1+1):
                arr1.append(A[index_2])
            arr.append(arr1)
    return arr  
'''
# A = [1, 2, 3]
A = [5, 2, 1, 4]
print(all_subarray(A))
'''


# ----------------------------------------------------------------------------------------------------------------------------------------

# Q6. Special Subsequences "AG" - 2

# Problem Description
# You have given a string A having Uppercase English letters.
# You have to find the number of pairs (i, j) such that A[i] = 'A', A[j] = 'G' and i < j.

    # Problem Constraints
    # 1 <= length(A) <= 105

# Input Format
# First and only argument is a string A.

# Output Format
# Return an long integer denoting the answer.

def S_subsequence(A):
    count_a = 0; ans = 0
    for item in A:
        if item == 'A':
            count_a+=1
        elif item == 'G':
            ans = ans+count_a
    return ans

''''
# A = "ABCGAG"
A = "ABAGGA"
print(S_subsequence(A))

''' 


# -------------------------------------------------------------------------------------------------------------------------------------------

# Q1. Pick from both sides!

# Problem Description
# You are given an integer array A of size N.
# You have to perform B operations. In one operation, you can remove either the leftmost or the rightmost element of the array A.
# Find and return the maximum possible sum of the B elements that were removed after the B operations.
# NOTE: Suppose B = 3, and array A contains 10 elements, then you can:

# Remove 3 elements from front and 0 elements from the back, OR
# Remove 2 elements from front and 1 element from the back, OR
# Remove 1 element from front and 2 elements from the back, OR
# Remove 0 elements from front and 3 elements from the back.

    # Problem Constraints
    # 1 <= N <= 105
    # 1 <= B <= N
    # -103 <= A[i] <= 103

# Input Format
# First argument is an integer array A.
# Second argument is an integer B.

# Output Format
# Return an integer denoting the maximum possible sum of elements you removed.


# -------------------------------------------------------------------------------------------------------------------------------

# Q2. Leaders in an array

# Problem Description
# Given an integer array A containing N distinct integers, you have to find all the leaders in array A. An element is a leader if it is strictly greater than all the elements to its right side.
# NOTE: The rightmost element is always a leader.

    # Problem Constraints
    # 1 <= N <= 105
    # 1 <= A[i] <= 108

# Input Format
# There is a single input argument which a integer array A

# Output Format
# Return an integer array denoting all the leader elements of the array.

def leadres(A):   #Brute force approach........  #Space complexity = O(N),    Time Complexity = O(n^2)
    arr = []; 
    for index in range(len(A)-1):
        Max = A[index]
        pre_max = Max
        for index_1 in range(index+1,len(A)):
            if A[index_1]>Max:
                Max = A[index_1]
        if pre_max == Max:
            arr.append(Max)
    arr.append(A[len(A)-1])
    return arr

def leader_optimized(A):    #Space complexity = O(N),    Time Complexity = O(n)
    leader = A[len(A)-1]
    arr = [leader]
    for index in range(len(A)-2,-1,-1):
        if A[index] > leader:
            leader = A[index]
            arr.append(leader)
    return arr
'''
# A = [16, 17, 4, 3, 5, 2]
A = [100,2,0,500,11,2,5,0]
print(leader_optimized(A))
'''




# ---------------------------------------------------------------------------------------------------------------------------------

# Q3. Best Time to Buy and Sell Stocks I

# Problem Description
# Say you have an array, A, for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
# Return the maximum possible profit.

    # Problem Constraints
    # 0 <= A.size() <= 700000
    # 1 <= A[i] <= 107

# Input Format
# The first and the only argument is an array of integers, A.

# Output Format
# Return an integer, representing the maximum possible profit.



def stocks(A):
    if len(A) < 2:
        return 0
    
    profit, buy = 0, A[0]
    for index in range(1,len(A)):
        if A[index] > profit:
            profit = A[index]
    profit = profit - buy
    return profit

'''
# A = [1, 2]
A = [1, 4, 5, 2, 4,10,100,0,2,3]
print(stocks(A))
'''


