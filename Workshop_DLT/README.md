#### Notes on Data Ingestion with dlt

#### Question 1
```
def square_root_generator(limit):
    n = 1
    while n <= limit:
        yield n ** 0.5
        n += 1
# Example usage:
limit = 5
generator = square_root_generator(limit)
# Sum of the outputs
sum_of_outputs = sum(generator)
print("Sum of square roots for limit =", limit, ":", sum_of_outputs)
```
