a = int(input())
# def count_fac(a):
#     i=1
#     factor = 0
#     while i*i <=a:
#         if a%i==0:
#             if i*i==a:
#                 factor+=1
#             else: factor+=2
#         i+=1
#     return factor

# def prime(a):
#     result = count_fac(a)
#     if result >2:
#         return 0
#     else: return 1
# print(prime(a))

# def perfect_sqr(a):
#     Sum=0
#     for i in range(1,int(a/2)+1):
#         if a%i==0:
#             Sum+=i
#     if Sum == a:
#         return 0
#     else: return 1
# print(perfect_sqr(a))


def is_prime(a):
    factor = 0
    for i in range(1,int(a**0.5)+1):
        if a%i == 0:
            if (i**2) == a:
                factor+=1
            else: factor+=2
    if factor <=2:
        return 0
    else: return 1

def solution(a):
    prime_count = 0
    for i in range(2,a+1):
        result = is_prime(i)
        if result == 0:
            if result <= a:
                prime_count +=1
    return prime_count

print(solution(a))



            





        
            
