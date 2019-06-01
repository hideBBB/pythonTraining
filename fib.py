def fib(n): # return Fibonacci series up to n
   result = []
   a, b = 0, 1
   while b < n:
      result.append(b)
      a, b = b, a + b

   print(locals())
   return result


def print_func( par ):
   print("Hello : ", par)
   # print(globals())
   print(locals())
   return

if __name__ == "__main__":
    f = fib(100)
    print(f)
    print(globals())


print_func("safd")

# f = fib(100)
# print(f)
