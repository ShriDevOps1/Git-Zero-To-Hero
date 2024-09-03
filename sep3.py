def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
    return sequence

# Example usage
num_terms = 10
fib_sequence = fibonacci(num_terms)

print(f"Fibonacci sequence with {num_terms} terms:")
print(fib_sequence)
