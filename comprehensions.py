# Comprehensions offer a flexible and more performant way to do some operations,
# that would require otherwise much longer code, and their computational cost would be higher

# There exist list, dictionary, set comprehensions and the value generator expressions.

# Definition: a comprehension applies a statement to an iterable

# Ex. of simplest list comprehension

In [126]: l = ['elena', 'maria', 'daria']

In [127]: [i.upper() for i in l]

# Out[127]: ['ELENA', 'MARIA', 'DARIA']

In [133]: s = ['hello', 'bye', 'good afternoon']

In [134]: [len(i) for i in s]

# Out[134]: [5, 3, 14]

# An alternative using a for loop in Python for the last example:
In [135]: res_list  = []

In [136]: for i in s:
     ...:     str_len = len(i)
     ...:     res_list.append(str_len)
     ...:     

In [137]: res_list
# Out[137]: [5, 3, 14]


# How are list comprehensions different from other functional programming tools?

In [158]: map(abs, [-1, 0, 1])
# Out[158]: [1, 0, 1]

In [159]: [abs(i) for i in [-1, 0, 1]]
# Out[159]: [1, 0, 1]

# In case we use a statement, however, map function becomes more complicated, we have to resort to lambda
In [164]: map(lambda x: x**3, [1, 2, 3])
# Out[164]: [1, 8, 27]

In [166]: [i**3 for i in [1, 2, 3]]
# Out[166]: [1, 8, 27]

# list comprehensions can be made even more generic, using the if clause
In [179]: x = range(0, 45, 2)

In [181]: [i for i in x if i % 3 == 0]

# EXERCISE: write the same using a for statement

# Comprehension syntax
# [expression for target1 in iterable1 if condition1
              # for target2 in iterable2 if condition2
              # for target3 in iterable3 if condition3 ...]
# these are nested for loop statements
In [182]: [i + j for i in range(10) for j in range(5)]
#EXERCISE1: how would you write the above using the for statements?

#EXERCISE2: make combinations of two characters from two words FINLAND and SUOMI
# e.g. FS, FU, FO, FM, FI, IS, ...

# Remember the KISS rule: keep it simple
# Simple is better than complex

# performance-wise, the following formula holds:
# for loops < map < list comprehension

# Main advantages of list comprehensions:
# * performance
# * conciseness
# * expressivenes - they are expressions, so can be used in the bodies of lambdas, within list, dictonaries, etc.



