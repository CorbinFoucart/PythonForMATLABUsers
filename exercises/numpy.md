
# micro-assignment 1: `NumPy` and reading documentation
Learning to read documentation is a skill that's just as important (if not more
important) than writing new code. This assignment can be thought of as a way to
practice working with `NumPy` and also to practice reading and understanding
documentation.

1. find the documentation for `numpy.random` and use it to learn how to generate random vectors and random matrices
2. read the documentation for `numpy.dot` and learn how to use it to multiply a random vector and random matrix of campatible size
3. implement a function `my_matmult` in your python script which computes matrix-vector multiplication for a vector of shape `(n,)` and numpy array of shape `(m,n)`. Compare your function's answer to the answer returned by `numpy.dot`. Your function might look like this:

```python
def my_matmult(A, x):
  """ returns the matrix-vector multiplication b = A*x """

  # my code here
  return b
```
4. (Bonus) Time the performance of your function compared to `numpy.dot` and print the results to console for several different sizes of `n`. You will need to look at the documentation for the `timeit` library (which is part of the standard library).
