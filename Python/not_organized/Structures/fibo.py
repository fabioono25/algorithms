from gc import callbacks

calls = 0

def fibonacci(n: int):
  global calls
  calls += 1

  if n == 0 or n == 1:
    return n

  return fibonacci(n -1) + fibonacci(n - 2)

print('result: ', fibonacci(35))
print('total calls: ', calls)

calls2 = 0

def fibonacciMemo(n: int, memo):
  global calls2
  calls2 += 1

  if not n in memo:
    memo[n] = fibonacciMemo(n - 1, memo) + fibonacciMemo(n - 2, memo)

  return memo[n]


memo = {0:0, 1:1} # now, we create a hash structure (dictionary) to use as cache
print('result with cache: ', fibonacciMemo(35, memo))
print('total calls with cache: ', calls2)
