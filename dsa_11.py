# Interview_Problems
# Q1. Length of longest consecutive ones
'''
Given a binary string A. It is allowed to do at most one swap between any 0 and 1. Find and return the length of the longest consecutive 1’s that can be achieved.
Input Format
The only argument given is string A.
Output Format
Return the length of the longest consecutive 1’s that can be achieved.
Constraints
1 <= length of string <= 1000000
A contains only characters 0 and 1.
For Exampl
Input 1:
    A = "111000"
Output 1:
    3
Input 2:
    A = "111011101"
Output 2:
    7
'''

def lconsecutiveOnes(A):#Space complexity = O(1),    Time Complexity = O(N)
    Count_1 = 0
    for item in A:
        if item == '1':
            Count_1+=1
    if Count_1 == 0:
        return 0
    elif Count_1 == len(A):
        return len(A)
    else:
        Ones = 0
        for index in range(len(A)):  # touching all the elements ==> O(N)  >> 2N >> O(N)
            if A[index] == '0':
                L = index-1; R = index+1; Count_L = Count_R = 0
                while (L>=0 and A[L]=='1'):   # Maximum touched element is 2
                    Count_L+=1; L-=1
                while (R<len(A) and A[R]=='1'): # Maximum touched element is 2
                    Count_R+=1; R+=1
                leftOver1 = Count_1-Count_L-Count_R
                if leftOver1 > 0:
                    Ones = max(Ones,Count_R+Count_L+1)
                else:
                    Ones = max(Ones,Count_R+Count_L)  
    return Ones
'''
A = "111000"
A = "111011101"
print(lconsecutiveOnes(A))
'''

# -------------------------------------------------------------------------------------------------------------
# Q2. Majority Element
'''
Problem Description
Given an array of size N, find the majority element. The majority element is the element that appears more than floor(n/2) times.
You may assume that the array is non-empty and the majority element always exists in the array.

Problem Constraints
1 <= N <= 5*105
1 <= num[i] <= 109

Input Format
Only argument is an integer array.
Output Format
Return an integer.

Example Input
Input 1:
[2, 1, 2]
Input 2:
[1, 1, 1]
Example Output
Input 1:
2
Input 2:
1
Example Explanation
For Input 1:
2 occurs 2 times which is greater than 3/2.
For Input 2:
 1 is the only element in the array, so it is majority
'''

def maorityElement(A): #Moore’s Voting Algorithm... #Space complexity = O(1),    Time Complexity = O(N)
    tem_arr = Count = freq = 0
    for index in range(len(A)):
        if Count == 0:
            tem_arr = A[index]
            Count+=1
        elif tem_arr == A[index]:
            Count+=1
        else: Count-=1
    for item in A:
        if item == tem_arr:
            freq+=1
    if freq > (len(A)/2):
        return tem_arr
    else: return len(A)
'''
A = [2, 1, 2]
A = [1, 1, 1]
print(maorityElement(A))
'''

# ----------------------------------------------------------------------------------------------------------------

def countInTriplets(self, A): #Pending........
    Count = 0
    for index in range(len(A)):
        pass
'''
def solve(self, A):
    n = len(A)
    ans = 0
    for i in range(n):
        l = 0
        r = 0
        for j in range(i):
            if A[j] < A[i]:
                l += 1
        for j in range(i + 1 , n):
            if(A[i] < A[j]):
                r += 1
        ans += (l * r)
    return ans
'''
# -------------------------------------------------------------------------------------------------------
# Q Given ar[N][M], if ar[i][j] == 0 make all elements in that row and column as 0.

def matrixZeros(A):#Space complexity = O(1),    Time Complexity = O(N^2)
    for rows in range(len(A)):
        flag = 0
        for columns in range(len(A[0])):
            if A[rows][columns] == 0:
                flag = 1
        if flag == 1:
            for columns in range(len(A[0])):
                if A[rows][columns] != 0:
                   A[rows][columns] = -1

    for columns in range(len(A[0])):
        flag = 0
        for rows in range(len(A)):
            if A[rows][columns] == 0:
                flag = 1
        if flag == 1:
            for rows in range(len(A)):
                if A[rows][columns] != 0:
                   A[rows][columns] = -1

    for rows in range(len(A)):
        for columns in range(len(A[0])):   
            if A[rows][columns] == -1:
               A[rows][columns] = 0

    return A
'''
A = [[1,2,3,4]
    ,[5,0,0,6],
     [7,8,9,10]]  
print(matrixZeros(A))
'''



         
                
        





# ----------------------------------------------------------------------------------------------------------
# Q1. N/3 Repeat Number
'''
Problem Description
You're given a read-only array of N integers. Find out if any integer occurs more than N/3 times in the array in linear time and constant additional space.
If so, return the integer. If not, return -1.
If there are multiple solutions, return any one.
Note: Read-only array means that the input array should not be modified in the process of solving the problem

Problem Constraints
1 <= N <= 7*105
1 <= A[i] <= 109

Input Format
The only argument is an integer array A.

Output Format
Return an integer.
Example Input
Input 1:
[1 2 3 1 1]
Input 2:
[1 2 3]
Example Output
Output 1:
1
Output 2:
-1

Example Explanation
Explanation 1:
1 occurs 3 times which is more than 5/3 times.
Explanation 2:
No element occurs more than 3 / 3 = 1 times in the array.
'''

def repeatNumber(A):#Moore’s Voting Algorithm... #Space complexity = O(1),    Time Complexity = O(N)
    tem_arr = Count = freq = 0
    for index in range(len(A)):
        if Count == 0:
            tem_arr = A[index]
            Count+=1
        elif tem_arr == A[index]:
            Count+=1
        else: Count-=1
    for item in A:
        if item == tem_arr:
            freq+=1
    if freq > (len(A)/3):
        return tem_arr
    else: return -1
'''
A = [1, 2,3, 1, 1]
A = [1, 2, 3]
print(repeatNumber(A))
'''
# --------------------------------------------------------------------------------------------------
# Q2. Check anagrams
'''
Problem Description
You are given two lowercase strings A and B each of length N. Return 1 if they are anagrams to each other and 0 if not.
Note : Two strings A and B are called anagrams to each other if A can be formed after rearranging the letters of B.

Problem Constraints
1 <= N <= 105
A and B are lowercase strings

Input Format
Both arguments A and B are a string.
Output Format
Return 1 if they are anagrams and 0 if not

Example Input
Input 1:
A = "cat"
B = "bat"
Input 2:
A = "secure"
B = "rescue"

Example Output
Output 1:
0
Output 2:
1
Example Explanation
For Input 1:
The words cannot be rearranged to form the same word. So, they are not anagrams.
For Input 2:
They are an anagram.
'''

def checkAnagrams(A,B):
    if len(A) != len(B):
        return 0
    else:
        for item in A:
            if item not in B:
                return 0
    return 1
'''
A = "cat"
B = "bat"
A = "secure"
B = "rescue"
print(checkAnagrams(A,B))
'''

# ---------------------------------------------------------------------------------------------------
# Q3. Colorful Number
'''
Problem Description
Given a number A, find if it is COLORFUL number or not.
If number A is a COLORFUL number return 1 else, return 0.
What is a COLORFUL Number:
A number can be broken into different consecutive sequence of digits. 
The number 3245 can be broken into sequences like 3, 2, 4, 5, 32, 24, 45, 324, 245 and 3245. 
This number is a COLORFUL number, since the product of every consecutive sequence of digits is different

Problem Constraints
1 <= A <= 2 * 109

Input Format
The first and only argument is an integer A.
Output Format
Return 1 if integer A is COLORFUL else return 0.

Example Input
Input 1:
 A = 23
Input 2:
 A = 236
Example Output
Output 1:
 1
Output 2:
 0

Example Explanation
Explanation 1:
 Possible Sub-sequences: [2, 3, 23] where
 2 -> 2 
 3 -> 3
 23 -> 6  (product of digits)
 This number is a COLORFUL number since product of every digit of a sub-sequence are different. 
Explanation 2:
 Possible Sub-sequences: [2, 3, 6, 23, 36, 236] where
 2 -> 2 
 3 -> 3
 6 -> 6
 23 -> 6  (product of digits)
 36 -> 18  (product of digits)
 236 -> 36  (product of digits)
 This number is not a COLORFUL number since the product sequence 23  and sequence 6 is same. 
 '''

def colorfulNumber(A):
    arr = []
    while A!=0:
        n = A%10
        arr.append(n)
        A//=10
    print(arr)
    N = len(arr)
    for start in range(N-1):
        product = 1
        for end in range(start,N):
            product*=arr[end]
        arr.append(product)
    print(arr)
    #finding duplicates......
    for index in range(len(arr)-1):
        for index_1 in range(index+1,len(arr)): 
            if arr[index] == arr[index_1]:
                return 0
    return 1
'''
# A = 23
A = 236
print(colorfulNumber(A))
'''
# --------------------------------------------------------------------------------------------------------------------------


