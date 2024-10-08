# ONE DIMENSIONAL Array

# Q1. Max Sum Contiguous Subarray

'''
Problem Description
Find the maximum sum of contiguous non-empty subarray within an array A of length N.

Problem Constraints
1 <= N <= 1e6
-1000 <= A[i] <= 1000

Input Format
The first and the only argument contains an integer array, A.
Output Format
Return an integer representing the maximum possible sum of the contiguous subarray.

Example Input
Input 1:
 A = [1, 2, 3, 4, -10] 
Input 2:
 A = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 

Example Output
Output 1:
 10 
Output 2:
 6 

Example Explanation
Explanation 1:
 The subarray [1, 2, 3, 4] has the maximum possible sum of 10. 
Explanation 2:
 The subarray [4,-1,2,1] has the maximum possible sum of 6. 

'''



# KADANES ALGO....
def maxSubarray(A): #Space complexity = O(1),    Time Complexity = O(N)
    local_max = global_max = A[0]
    for index in range(1,len(A)):
        if local_max < 0:
            local_max = 0
        local_max+=A[index]
        if global_max < local_max:
            global_max = local_max
    return global_max
'''
A = [1, 2, 3, 4, -10]
A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubarray(A))
'''

# -----------------------------------------------------------------------------------------------------------
# Q2. Continuous Sum Query

'''
Problem Description
There are A beggars sitting in a row outside a temple. Each beggar initially has an empty pot. When the devotees come to the temple, they donate some amount of coins to these beggars. Each devotee gives a fixed amount of coin(according to their faith and ability) to some K beggars sitting next to each other.
Given the amount P donated by each devotee to the beggars ranging from L to R index, where 1 <= L <= R <= A, find out the final amount of money in each beggar's pot at the end of the day, provided they don't fill their pots by any other means.
For ith devotee B[i][0] = L, B[i][1] = R, B[i][2] = P, given by the 2D array B

Problem Constraints
1 <= A <= 2 * 105
1 <= L <= R <= A
1 <= P <= 103
0 <= len(B) <= 105

Input Format
The first argument is a single integer A.
The second argument is a 2D integer array B.
Output Format
Return an array(0 based indexing) that stores the total number of coins in each beggars pot.

Example Input
Input 1:-
A = 5
B = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
Example Output
Output 1:-
10 55 45 25 25

Example Explanation
Explanation 1:-
First devotee donated 10 coins to beggars ranging from 1 to 2. Final amount in each beggars pot after first devotee: [10, 10, 0, 0, 0]
Second devotee donated 20 coins to beggars ranging from 2 to 3. Final amount in each beggars pot after second devotee: [10, 30, 20, 0, 0]
Third devotee donated 25 coins to beggars ranging from 2 to 5. Final amount in each beggars pot after third devotee: [10, 55, 45, 25, 25]
'''


def cSumQuery(A,B):#Space complexity = O(1),    Time Complexity = O(N)
    A = [0]*A
    for index in range(len(B)):
        s = B[index][0]; e = B[index][1]; value = B[index][2]
        A[s-1] += value 
        if e < len(A):
            A[e] -=(value)
    # find prefixSum for the above array
    for index in range(1,len(A)):
        A[index] += A[index-1] 
    return A
'''
A = 5
B = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
print(cSumQuery(A,B))
'''
# -----------------------------------------------------------------------------------------------
# Q3. Rain Water Trapped

'''
Problem Description
Imagine a histogram where the bars' heights are given by the array A. Each bar is of uniform width, which is 1 unit. When it rains, water will accumulate in the valleys between the bars.
Your task is to calculate the total amount of water that can be trapped in these valleys.

Example:
The Array A = [5, 4, 1, 4, 3, 2, 7] is visualized as below. The total amount of rain water trapped in A is 11.
Rain Water Trapped
Problem Constraints
1 <= |A| <= 105
0 <= A[i] <= 105

Input Format
First and only argument is the Integer Array, A.
Output Format
Return an Integer, denoting the total amount of water that can be trapped in these valleys

Example Input
Input 1:
 A = [0, 1, 0, 2]
Input 2:
A = [1, 2]

Example Output
Output 1:
1
Output 2:
0

Example Explanation
Explanation 1:
1 unit is trapped on top of the 3rd element.
Rain Water Histogram
Explanation 2:
No water is trapped.
'''


def rainWaterTrapped(A):#Space complexity = O(N),    Time Complexity = O(N)
    # finding left max building (prefix)
    prefix = []
    prefix.append(A[0])
    for index in range(1,len(A)):
        M = max(prefix[index-1],A[index])
        prefix.append(M)
    # finding right max building (sufix)
    sufix = list(A)
    for index in range(len(A)-2,-1,-1):
        sufix[index] = max(sufix[index+1],sufix[index])
    # finding rain water trapped in a building
    ans = 0
    for index in range(1,len(A)-1):
        Sum = min(prefix[index-1],sufix[index+1])-A[index]
        if Sum > 0:
            ans+=Sum
    return ans

def rainWaterTrapped1(A): #optimized code  #Space complexity = O(1),    Time Complexity = O(N)
    l=0; r= len(A)-1; ans =0; lmax = rmax = 0
    while l<r:
        if lmax < A[l]:
            lmax = A[l]
        if rmax < A[r]:
            rmax = A[r]
        
        if lmax < rmax:
            ans+=lmax-A[l]
            l+=1    
        else:
            ans+=rmax-A[r]
            r-=1
    return ans



A = [0, 1, 0, 2]
A = [0,1,0,2,1,0,1,3,2,1,2,1]
print(rainWaterTrapped(A))

# --------------------------------------------------------------------------------------------------
# Q1. Add One To Number

'''
Problem Description

Given a non-negative number represented as an array of digits, add 1 to the number ( increment the number represented by the digits ).
The digits are stored such that the most significant digit is at the head of the list.
NOTE: Certain things are intentionally left unclear in this question which you should practice asking the interviewer. For example: for this problem, the following are some good questions to ask :
Q: Can the input have 0's before the most significant digit. Or, in other words, is 0 1 2 3 a valid input?
A: For the purpose of this question, YES
Q: Can the output have 0's before the most significant digit? Or, in other words, is 0 1 2 4 a valid output?
A: For the purpose of this question, NO. Even if the input has zeroes before the most significant digit.

Problem Constraints
1 <= size of the array <= 1000000

Input Format
First argument is an array of digits.
Output Format
Return the array of digits after adding one.

Example Input
Input 1:
[1, 2, 3]

Example Output
Output 1:
[1, 2, 4]

Example Explanation
Explanation 1:
Given vector is [1, 2, 3].
The returned vector should be [1, 2, 4] as 123 + 1 = 124.
'''
def addOne(A):  #Pending........
    N = A; result = 0
    for item in range(len(A),-1,-1):
        r = item%10
        result =result*10 + r
    A[len(A)-1] = result
    return A
'''
A = [1, 2, 3]
print(addOne(A))
'''
# ------------------------------------------------------------------
# Q2. Flip

'''
Problem Description
You are given a binary string A(i.e., with characters 0 and 1) consisting of characters A1, A2, ..., AN. In a single operation, you can choose two indices, L and R, such that 1 ≤ L ≤ R ≤ N and flip the characters AL, AL+1, ..., AR. By flipping, we mean changing character 0 to 1 and vice-versa.
Your aim is to perform ATMOST one operation such that in the final string number of 1s is maximized.
If you don't want to perform the operation, return an empty array. Else, return an array consisting of two elements denoting L and R. If there are multiple solutions, return the lexicographically smallest pair of L and R.
NOTE: Pair (a, b) is lexicographically smaller than pair (c, d) if a < c or, if a == c and b < d.

Problem Constraints
1 <= size of string <= 100000

Input Format
First and only argument is a string A.
Output Format
Return an array of integers denoting the answer.

Example Input
Input 1:
A = "010"
Input 2:
A = "111"
Example Output
Output 1:
[1, 1]
Output 2:
[]

Example Explanation
Explanation 1:
A = "010"
Pair of [L, R] | Final string
_______________|_____________
[1 1]          | "110"
[1 2]          | "100"
[1 3]          | "101"
[2 2]          | "000"
[2 3]          | "001"
We see that two pairs [1, 1] and [1, 3] give same number of 1s in final string. So, we return [1, 1].
Explanation 2:
No operation can give us more than three 1s in final string. So, we return empty array [].
'''
def filp(A):
    arr = [0]*2; l = r= 0; lSum = gsum = 0
    for item in A:
        if item == '1':
            lSum-=1
        else: lSum+=1
        if lSum > gsum:
            gsum = lSum
            arr[1] = r+1
            arr[0] = l+1
        if lSum < 0:
            lSum = 0 
            l+=1; r+=1
        else:
            r+=1
    if gsum < 1:
        return []
    else: return arr
'''
A = "010"
A = "111"
print(filp(A))
'''
# ------------------------------------------------------------------------------------------------------------------------

    




