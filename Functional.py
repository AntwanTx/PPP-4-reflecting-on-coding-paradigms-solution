# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

def flatten_and_sort(array):
    flattened = [num for sublist in arr for num in sublist]
    return sorted(flattened)
print(flatten_and_sort([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

'''
Make sure to answer the following questions about your coding process:

How does this solution ensure data immutability? The original array is not modified, a new one is returned.

Is this solution a pure function? Why or why not? Yes, this is pure. It always gives the same result.

Is this solution a higher order function? Why or why not? No, this is not a higher order function. It does not return anything.

Would it have been easier to solve this problem using a different programming style? Depending on the user, OOP could be easier to implement.

Why in particular is functional programming a helpful paradigm when solving this problem? Functional programming is helpful here because it allows for easy chaining of operations and ensures that original data remains unmodified.
'''
