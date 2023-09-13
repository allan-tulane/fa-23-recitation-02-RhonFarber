"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
import math
###


def simple_work_calc(n, a, b):
  """Compute the value of the recurrence $W(n) = aW(n/b) + n
  
	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor

	Returns: the value of W(n).
	"""
  if n < b:
    return n
  return a * simple_work_calc(n / b, a, b) + n


def work_calc(n, a, b, f):
  """Compute the value of the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
  
  if n <= 1:
    return f(n)
  else:
    return a * work_calc(n / b, a, b, f) + f(n)

  # create new lambda function in main or test function
  # plugging in 
# Actual Values for #4
print("Evidence:")
print("f(n) = 1")
print(work_calc(10, 2, 2, lambda n: 1))
print(work_calc(20, 2, 2, lambda n: 1))
print(work_calc(100, 2, 2, lambda n: 1))
print(work_calc(1000, 2, 2, lambda n: 1))
print(work_calc(2000, 2, 2, lambda n: 1))
print(work_calc(10000, 2, 2, lambda n: 1))
print("\n")

print("Evidence:")
print("f(n) = log(n)")
print(work_calc(10, 2, 2, lambda n: math.log(n)))
print(work_calc(20, 2, 2, lambda n: math.log(n)))
print(work_calc(100, 2, 2, lambda n: math.log(n)))
print(work_calc(1000, 2, 2, lambda n: math.log(n)))
print(work_calc(2000, 2, 2, lambda n: math.log(n)))
print(work_calc(10000, 2, 2, lambda n: math.log(n)))
print("\n")

print("Evidence:")
print("f(n) = n")
print(work_calc(10, 2, 2, lambda n: n))
print(work_calc(20, 2, 2, lambda n: n))
print(work_calc(100, 2, 2, lambda n: n))
print(work_calc(1000, 2, 2, lambda n: n))
print(work_calc(2000, 2, 2, lambda n: n))
print(work_calc(10000, 2, 2, lambda n: n))

def span_calc(n, a, b, f):
  """Compute the span associated with the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
  if n <= 1:
    return 1
  else:
    return a * span_calc(n/b, a, b, f) + 1


def compare_work(work_fn1,
                 work_fn2,
                 sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
  """
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
  result = []
  for n in sizes:
    # compute W(n) using current a, b, f
    result.append((n, work_fn1(n), work_fn2(n)))
  return result

def print_results(results):
  """ done """
  print(
      tabulate.tabulate(results,
                        headers=['n', 'W_1', 'W_2'],
                        floatfmt=".3f",
                        tablefmt="github"))


def test_compare_work():
  # curry work_calc to create multiple work
  # functions that can be passed to compare_work

  # create work_fn1
  # create work_fn2

  # 
  work_fn1 = lambda n: work_calc(n, 2, 2, lambda x: x**0.5)
  work_fn2 = lambda n: work_calc(n, 2, 2, lambda x: x**1.5)
  
  res = compare_work(work_fn1, work_fn2)
  print(res)

test_compare_work()

def compare_span(span_fn1, span_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
  """
  Compare the values of different recurrences for
  given input sizes.
  Returns:
  A list of tuples of the form
  (n, work_fn1(n), work_fn2(n), ...)
  """
  result = []
  for n in sizes:
    # compute W(n) using current a, b, f
    result.append((
          n,
          span_fn1(n),
          span_fn2(n)
          ))
  return result


def test_compare_span():
  def span_fn1(n):
    return span_calc(n, 4, 2, lambda n:math.pow(n, 1.0))
  def span_fn2(n):
    return span_calc(n, 4, 2, lambda n:math.pow(n, 10.0))
  res = compare_span(span_fn1, span_fn2)
  print(res)

test_compare_span()