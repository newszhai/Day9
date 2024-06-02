# x=int(input())
# def F(x):
#     if x>=2:
#         return F(x-1)+F(x-2)
#     else:
#         return x
# print(F(x))

def fibo(n):
    if n ==1 or n==2:
      return 1
    else:
      return fibo(n-1)+fibo(n-2)
print(fibo(1))