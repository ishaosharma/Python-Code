#Generator Expressions: A concise way to create generators, similar to list comprehensions
# but with parentheses.

squares = (x * x for x in range(5))
for square in squares:
    print(square)
