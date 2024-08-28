def factor(A):
    fac = 0
    i = 1
    while i*i <= A:
        if A%i==0:
            if i == A:
                fac+=1
            else: fac+=2
        i+=1
    return fac
# print(factor(5))

def prime(A):
    a  = factor(A)
    if a > 2:
        return 0
    else: 
        return 1
# print(prime(11))

def perfect_no(A):
    Sum =0
    for index in range(1,A//2+1):
        Sum+=index
    if Sum == A:
        return 1
    else: return 0
# print(perfect_no(6))

def prime_no(A):
    prime_count = 0
    for index in range(2,A+1):
        result = prime(index)
        if result == 1:
            prime_count+=1
    return prime_count
# print(prime_no(5))


def good_pair(A,B):
    for index in range(len(A)-1):
        for index_1 in range(index+1,len(A)):
            if A[index] + A[index_1] == B:
                return 1
    return 0
'''
# A = [1,2,3,4]
# B = 7

# A = [1,2,4]
# B = 4

A = [1,2,2]
B = 4
print(good_pair(A,B))
'''

def reverse(A,B,C):
    start = B; end = C
    while start < end:
        temp = A[B]
        A[B] = A[C]
        A[C] = temp
        start+=1; end-=1
    return A

# A = [1,2,3,4,5]
# B = 2
# C = 3
# A = [2, 5, 6]
B = 0
C = 2
# print(reverse(A,B,len(A)-1))
# print(reverse(A,0,4))
'''
def rotate(A,B):
    N = len(A)
    if B>N:
        B = B%N
    reverse(A,0,N-1)
    print(A)
    reverse(A,0,B-1)
    reverse(A,B,N-1)
    return A
A = [1, 2, 3, 4]
B = 2
print(rotate(A,B))
'''

def Sum_max_min(A):
    Min = Max = A[0]
    for item in A:
        if item < Min:
            Min = item
        if item > Max:
            Max = item
    return (Min + Max)
'''
# A = [-2, 1, -4, 5, 3]
A = [1, 3, 4, 1]

print(Sum_max_min(A))
'''

def occurrences(A,B):
    Count = 0
    for item in A:
        if B == item:
            Count+=1
    return Count
'''
# A = [1, 2, 2]; B = 2 
A = [1, 2, 1]; B = 3 
print(occurrences(A,B))
'''


def timeEquality(A):
    m = max(A); Sum = 0
    for item in A:
        Sum+=(m-item)
    return Sum
'''
A = [2, 4, 1, 3, 2]
print(timeEquality(A))
'''

def greater_check(A):
    m = max(A); Count =0
    for item in A:
        if item == m:
            continue
        else: Count+=1
    return Count
'''
A = [5, 5, 3]
print(greater_check(A))
'''


def second_largest(A):
    m=A[0]; sm = -1
    # m = max(A); sm = -1
    for item in A:
        if item > m:
            sm = m
            m = item
        elif item > sm and item!=m:
            sm = item
    return sm
'''
# A = [2, 1, 2] 
A = [2]
print(second_largest(A))
'''

def prefixSum(A):
    arr = []
    arr.append(A[0])
    for index in range(1,len(A)):
        Sum = arr[index-1] + A[index]
        arr.append(Sum)
    return arr

def rangeSumQuery(A,B):
    A = prefixSum(A)
    for index in range(len(B)):
        L = B[index][0]; R = B[index][1];
        if L > 0:
            Sum = A[R] - A[L-1]
            print(Sum, end=" ")
        else: Sum = A[R]; print(Sum, end=" ")
    print()
'''
# A = [1, 2, 3, 4, 5]
# B = [[0, 3], [1, 2]]
A = [2, 2, 2]
B = [[0, 0], [1, 2]]
rangeSumQuery(A,B)
'''


def even_odd_indices(A,type):
    arr = []
    if type.upper() == 'ODD':
        arr.append(0)
        for index in range(1,len(A)):
            if index %  2!=0:
                Sum = arr[index-1] + A[index]
                arr.append(Sum)
            else: Sum = arr[index-1]; arr.append(Sum)
    elif type.upper() == 'EVEN':
        arr.append(A[0])
        for index in range(1,len(A)):
            if index %  2==0:
                Sum = arr[index-1] + A[index]
                arr.append(Sum)
            else: Sum = arr[index-1]; arr.append(Sum)
    return arr

def Special_Index(A):
    odd = even_odd_indices(A,'odd')
    even = even_odd_indices(A,'even')
    result = 0
    for index in range(len(A)):
        if (index > 0):
            S_E = even[index-1] + odd[len(A)-1] - odd[index]
            S_O = odd[index-1] + even[len(A)-1] - even[index]
        else:
            S_E = even[len(A)-1] - even[index]; S_O = odd[len(A)-1] - odd[index]
        if S_O == S_E:
            result+=1
    return result
'''
# A = [2, 1, 6, 4]
A = [1, 1, 1]
print(Special_Index(A))
'''

def prefixSum_same_array(A):
    for index in range(1,len(A)):
        A[index] = A[index-1] + A[index]
    return A

def equilibrium(A):
    pre_Sum = prefixSum_same_array(A)
    for index in range(len(A)):
        if index > 0 and index<len(A)-1:
            L = pre_Sum[index-1]
            R_L = pre_Sum[index]
            R_R = pre_Sum[len(A)-1]
            Sum  = R_R - R_L
            if Sum == L:
                return index
    return -1
'''
# A = [-7, 1, 5, 2, -4, 3, 0]
A = [1,2,3,7,1,2,3]
print(equilibrium(A))
'''

def Closest(A):
    MIN = min(A)
    MAX = max(A)
    min_i = max_i = -1; ans = 10**9
    for index in range(len(A)):
            if A[index] == MAX:
                max_i = index
                if min_i != -1:
                    ans = min(ans,abs(min_i-max_i)+1)
            elif A[index] == MIN:
                min_i = index
                if max_i != -1:
                    ans = min(ans,abs(min_i-max_i)+1)
    return ans
'''
# A = [1, 3, 2]
A = [2, 6, 1, 6, 9]
print(Closest(A))
'''

def Subarray(A,B,C):
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
print(Subarray(A,B,C))
'''

def G_subarrays(A):
    arr = []
    for Start in range(len(A)):
        for end in range(Start,len(A)):
            arr1 = []
            for index in range(Start,end+1):
                arr1.append(A[index])
            arr.append(arr1)
    return arr

# A = [1, 2, 3]
A = [5, 2, 1, 4]
print(G_subarrays(A))






