'''
# Q1. Maximum Subarray Easy
# Problem Description
# You are given an integer array C of size A. Now you need to find a subarray (contiguous elements) so that the sum of contiguous elements is maximum.
# But the sum must not exceed B.


    # Problem Constraints
    # 1 <= A <= 103
    # 1 <= B <= 109
    # 1 <= C[i] <= 106

# Input Format
# The first argument is the integer A.
# The second argument is the integer B.
# The third argument is the integer array C.

Output Format
Return a single integer which denotes the maximum sum.

Example Input
Input 1:
A = 5
B = 12
C = [2, 1, 3, 4, 5]
Input 2:
A = 3
B = 1
C = [2, 2, 2]

Example Output
Output 1:
12
Output 2:
0

Example Explanation
Explanation 1:
We can select {3,4,5} which sums up to 12 which is the maximum possible sum.
Explanation 2:
All elements are greater than B, which means we cannot select any subarray.
Hence, the answer is 0.
'''


def max_subarray(A,B,C):   #Brute force approach........  #Space complexity = O(1),    Time Complexity = O(n^3)
    max_sub = -10**9; 
    for Start in range(A):
        for end in range(Start+1,A+1):
            Sum = 0
            for index in range(Start,end):
                Sum += C[index]
            if Sum > max_sub and Sum <= B:
                max_sub = Sum
            
    if max_sub > 0:
        return max_sub
    else: return 0

def pre_fix(A):
    arr = []
    arr.append(A[0])
    for index in range(1,len(A)):
        Sum = arr[index-1] + A[index]
        arr.append(Sum)
    return arr


def max_subarray1(A,B,C):  #prefix sum approach........  #Space complexity = O(N),    Time Complexity = O(n^2)
    arr = pre_fix(C); max_sub = -10**9
    for Start in range(A):
        Sum = 0
        for end in range(Start, A):
            if Start > 0:
                Sum = arr[end]-arr[Start-1]
            else: Sum = arr[end]
            if Sum > max_sub and Sum <= B:
                max_sub = Sum
    if max_sub > 0:
        return max_sub
    else: return 0

def max_subarray2(A,B,C): #Carry forward approach........  #Space complexity = O(1),    Time Complexity = O(n^2)
    max_sum = -10**9
    for index in range(A):
        Sum = 0
        for index_1 in range(index, A):
            Sum+=C[index_1]
            if Sum > max_sum and Sum <= B:
                    max_sum = Sum
    if max_sum > 0:
        return max_sum
    else: return 0


    
'''
        
A = 9
B = 14
C = [1,2,4,4,5,5,5,7,5]

# A = 1
# B = 75
# C = [1, 2, 3]

print(max_subarray2(A,B,C))'''

# -------------------------------------------------------------------------------------------------------------------------------
'''
Problem Description
You are given an integer array A of length N.
You have to find the sum of all subarray sums of A.
More formally, a subarray is defined as a contiguous part of an array which we can obtain by deleting zero or more elements from either end of the array.
A subarray sum denotes the sum of all the elements of that subarray.
Note : Be careful of integer overflow issues while calculations. Use appropriate datatypes.

Problem Constraints
1 <= N <= 105
1 <= Ai <= 10 4

Input Format
The first argument is the integer array A.

Output Format
Return a single integer denoting the sum of all subarray sums of the given array.

Example Input
Input 1:
A = [1, 2, 3]
Input 2:
A = [2, 1, 3]

Example Output
Output 1:
20
Output 2:
19

Example Explanation
Explanation 1:
The different subarrays for the given array are: [1], [2], [3], [1, 2], [2, 3], [1, 2, 3].
Their sums are: 1 + 2 + 3 + 3 + 5 + 6 = 20
Explanation 2:
The different subarrays for the given array are: [2], [1], [3], [2, 1], [1, 3], [2, 1, 3].
Their sums are: 2 + 1 + 3 + 3 + 4 + 6 = 19
'''
def subarraySum(A): #contribution approach........  #Space complexity = O(1),    Time Complexity = O(n)
    ans = 0
    for index in range(len(A)):
        ans += (index+1) * (len(A)-index) * A[index]
    return ans
'''
A = [1, 2, 3]
print(subarraySum(A))
    
'''

# ----------------------------------------------------------------------------------------------------
'''
Problem Description
Given an array A of length N. Also given are integers B and C.
Return 1 if there exists a subarray with length B having sum C and 0 otherwise

Problem Constraints
1 <= N <= 105
1 <= A[i] <= 104
1 <= B <= N
1 <= C <= 109

Input Format
First argument A is an array of integers.
The remaining arguments B and C are integers

Output Format
Return 1 if such a subarray exist and 0 otherwise

Example Input
Input 1:
A = [4, 3, 2, 6, 1]
B = 3
C = 11
Input 2:
A = [4, 2, 2, 5, 1]
B = 4
C = 6
Example Output
Output 1:
1
Output 2:
0
Example Explanation
Explanation 1:
The subarray [3, 2, 6] is of length 3 and sum 11.
Explanation 2:
There are no such subarray.
'''


def subarraySum_b(A,B,C):
    Sum = 0
    for index in range(B):
        Sum += A[index]
    ans = Sum

    Start = 1; end = B  
    while(end<len(A)):
        Sum += A[end] - A[Start-1]
        if C == Sum:
            return 1
        Start+=1;end+=1
    if C == Sum:
        return 1
    else: return 0
'''
A = [6]
B = 1
C = 6

print(subarraySum_b(A,B,C))
'''

# ---------------------------------------------------------------------------------------------------------------------------------------
'''
Problem Description
Given an array of integers A, a subarray of an array is said to be good if it fulfills any one of the criteria:
1. Length of the subarray is be even, and the sum of all the elements of the subarray must be less than B.
2. Length of the subarray is be odd, and the sum of all the elements of the subarray must be greater than B.
Your task is to find the count of good subarrays in A.

Problem Constraints
1 <= len(A) <= 5 x 103
1 <= A[i] <= 103
1 <= B <= 107

Input Format
The first argument given is the integer array A.
The second argument given is an integer B.
Output Format
Return the count of good subarrays in A.

Example Input
Input 1:
A = [1, 2, 3, 4, 5]
B = 4
Input 2:
A = [13, 16, 16, 15, 9, 16, 2, 7, 6, 17, 3, 9]
B = 65

Example Output
Output 1:
6
Output 2:
36
Example Explanation
Explanation 1:
Even length good subarrays = {1, 2}
Odd length good subarrays = {1, 2, 3}, {1, 2, 3, 4, 5}, {2, 3, 4}, {3, 4, 5}, {5} 
Explanation 1:
There are 36 good subarrays
'''
def goodSubarray(A,B): #Carry forward approach........  #Space complexity = O(1),    Time Complexity = O(n^2)
    Count=0
    for index in range(len(A)):
        Sum = 0 
        for index_1 in range(index,len(A)):
            Sum+=A[index_1]
            length = index_1 - index + 1
            if (length % 2 == 0 and Sum < B) or (length%2 != 0 and Sum > B):
                Count+=1
    return Count

'''
# A = [1, 2, 3, 4, 5]
# B = 4

A = [13, 16, 16, 15, 9, 16, 2, 7, 6, 17, 3, 9]
B = 65
print(goodSubarray(A,B))
'''
# -------------------------------------------------------------------------------------------------------------------------------------

'''
Problem Description
Given an array A of size N, find the subarray of size B with the least average.
Problem Constraints
1 <= B <= N <= 105
-105 <= A[i] <= 105

Input Format
First argument contains an array A of integers of size N.
Second argument contains integer B.
Output Format
Return the index of the first element of the subarray of size B that has least average.
Array indexing starts from 0.

Example Input
Input 1:
A = [3, 7, 90, 20, 10, 50, 40]
B = 3
Input 2:
A = [3, 7, 5, 20, -10, 0, 12]
B = 2

Example Output
Output 1:
3
Output 2:
4

Example Explanation
Explanation 1:
Subarray between indexes 3 and 5
The subarray {20, 10, 50} has the least average 
among all subarrays of size 3.
Explanation 2:
 Subarray between [4, 5] has minimum average
'''



def subarray_least( A,B):#sliding window approach........  #Space complexity = O(1),    Time Complexity = O(n)
    Sum = 0; result = 0 
    for index in range(B):
        Sum+=A[index]
    ans = Sum; start = 0; end = B
    for index in range(B,len(A)):
        Sum += A[index] - A[index-B]
        if ans > Sum:
            ans = Sum
            result = index - B +1
    return result

def subarray_least1( A,B):
    Sum = 0; result = 0 
    for index in range(B):
        Sum+=A[index]
    ans = Sum; start = 0; end = B
    while (end < len(A)):
        Sum += A[end] - A[start]
        if ans > Sum:
            ans = Sum
            result = start+1
        start+=1; end+=1
    return result
'''
# A = [3, 7, 90, 20, 10, 50, 40]
# B = 3

A = [3, 7, 5, 20, -10, 0, 12]
B = 2

print(subarray_least(A,B))
'''

# -----------------------------------------------------------------------------------------------------------------------------------------
'''
Problem Description
Given an array A of N non-negative numbers and a non-negative number B,
you need to find the number of subarrays in A with a sum less than B.
We may assume that there is no overflow.
Problem Constraints
1 <= N <= 5 x 103
1 <= A[i] <= 1000
1 <= B <= 107

Input Format
First argument is an integer array A.
Second argument is an integer B.

Output Format
Return an integer denoting the number of subarrays in A having sum less than B.

Example Input
Input 1:
 A = [2, 5, 6]
 B = 10
Input 2:
 A = [1, 11, 2, 3, 15]
 B = 10

Example Output
Output 1:
 4
Output 2:
 4

Example Explanation
Explanation 1:
 The subarrays with sum less than B are {2}, {5}, {6} and {2, 5},
Explanation 2:
 The subarrays with sum less than B are {1}, {2}, {3} and {2, 3}
'''

def minSubarry(A,B):
    Count=0
    for index in range(len(A)):
        Sum = 0
        for index_1 in range(index,len(A)):
            Sum+=A[index_1]
            if B > Sum:
                Count+=1
    return Count
'''
# A = [2, 5, 6]
# B = 10

A = [1, 11, 2, 3, 15]
B = 10
print(minSubarry(A,B))
'''

def sumSubarray(A):
    Sum = 0
    for Start in range(len(A)):
        for end in range(Start+1,len(A)+1):
            for index in range(Start,end):
                Sum += A[index]
    return Sum
'''
A = [1,2,3]
print(sumSubarray(A))
'''

