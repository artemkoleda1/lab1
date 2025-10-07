from sys import getsizeof
a = 3**9090001
b= float(getsizeof(a))
print((b/1024/1024))