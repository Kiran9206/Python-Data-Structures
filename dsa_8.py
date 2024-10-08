# Sorting


# Q1. Elements Removal
'''
Problem Description
Given an integer array A of size N. You can remove any element from the array in one operation.
The cost of this operation is the sum of all elements in the array present before this operation.
Find the minimum cost to remove all elements from the array.
Problem Constraints
0 <= N <= 1000
1 <= A[i] <= 103

Input Format
First and only argument is an integer array A.
Output Format
Return an integer denoting the total cost of removing all elements from the array.

Example Input
Input 1:
 A = [2, 1]
Input 2:
 A = [5]

Example Output
Output 1:
 4
Output 2:
 5

Example Explanation
Explanation 1:
 Given array A = [2, 1]
 Remove 2 from the array => [1]. Cost of this operation is (2 + 1) = 3.
 Remove 1 from the array => []. Cost of this operation is (1) = 1.
 So, total cost is = 3 + 1 = 4.
Explanation 2:
 There is only one element in the array. So, cost of removing is 5.

'''

def elemRemoval(A): #Carry forward approach........  #Space complexity = O(N),    Time Complexity = O(NLOGN)
    Sum=0
    A = sorted(A,reverse=True)  #THIS TAKES O(NLOGN) Time Complexity AND O(N)Space complexity
    for index in range(len(A)):
        Sum+=(index+1)*(A[index])
    return Sum
'''
A = [2, 1]
print(elemRemoval(A))
'''

# -------------------------------------------------------------------------------------------------------

# Q2. Noble Integer

'''
Problem Description
Given an integer array A, find if an integer p exists in the array such that the number of integers greater than p in the array equals p.

Problem Constraints
1 <= |A| <= 2*105
-108 <= A[i] <= 108

Input Format
First and only argument is an integer array A.
Output Format
Return 1 if any such integer p is present else, return -1.

Example Input
Input 1:
 A = [3, 2, 1, 3]
Input 2:
A = [1, 1, 3, 3]

Example Output
Output 1:
 1
Output 2:
 -1

Example Explanation
Explanation 1:
 For integer 2, there are 2 greater elements in the array..
Explanation 2:
 There exist no integer satisfying the required conditions.
'''

def nobleInteger(A):
    Count=0
    A = sorted(A,reverse=True)
    if A[0] == 0:
        return 1
    for index in range(1,len(A)):
        if A[index-1] != A[index]:
            Count = index
        if Count == A[index]:
            return 1
    return -1
'''
A = [3, 2, 1, 3]
print(nobleInteger(A))
'''
# ----------------------------------------------------------------------------------------------------------------------------------

# Q4. Kth Smallest Element

'''
Problem Description
Find the Bth smallest element in given array A .
NOTE: Users should try to solve it in less than equal to B swaps.
Problem Constraints
1 <= |A| <= 100000
1 <= B <= min(|A|, 500)
1 <= A[i] <= 109

Input Format
The first argument is an integer array A.
The second argument is integer B.
Output Format
Return the Bth smallest element in given array.

Example Input
Input 1:
A = [2, 1, 4, 3, 2]
B = 3
Input 2:
A = [1, 2]
B = 2
Example Output
Output 1:
 2
Output 2:
 2
Example Explanation
Explanation 1:
 3rd element after sorting is 2.
Explanation 2:
 2nd element after sorting is 2.
'''

def smallestElement(A,B):
    A = sorted(A); s = 0
    if B>=0:
        return A[B-1]
    return s
'''
A = [2, 1, 4, 3, 2]
B = 3
print(smallestElement(A,B))
'''
# ---------------------------------------------------------------------------------------------------------------------------------

# Q1. Arithmetic Progression?

'''
Problem Description
Given an integer array A of size N. Return 1 if the array can be arranged to form an arithmetic progression, otherwise return 0.
A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Problem Constraints
2 <= N <= 105
-109 <= A[i] <= 109

Input Format
The first and only argument is an integer array A of size N.
Output Format
Return 1 if the array can be rearranged to form an arithmetic progression, otherwise return 0.

Example Input
Input 1:
 A = [3, 5, 1]
Input 2:
 A = [2, 4, 1]

Example Output
Output 1:
 1
Output 2:
 0

Example Explanation
Explanation 1:
 We can reorder the elements as [1, 3, 5] or [5, 3, 1] with differences 2 and -2 respectively, between each consecutive elements.
Explanation 2:
 There is no way to reorder the elements to obtain an arithmetic progression.
'''

def aprogression(A):
    A = sorted(A)
    ans = A[1] - A[0]
    for index in range(2,len(A)):
        dif = A[index] - A[index-1]
        if dif != ans:
            return 0
    return 1
'''
A = [3, 5, 1]
A = [2, 4, 1]
print(aprogression(A))
'''


        

