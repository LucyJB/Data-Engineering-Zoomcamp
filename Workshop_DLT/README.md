### Notes on Data Ingestion with dlt

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
#### Question 2
```
def square_root_generator(limit):
    n = 1
    while n <= limit:
        yield n ** 0.5
        n += 1

# Example usage:
limit = 13
generator = square_root_generator(limit)

for sqrt_value in generator:
    print(sqrt_value)
```
#### Question 3
```
pip install duckdb
import duckdb

# Connect to DuckDB in-memory database
con = duckdb.connect(database=':memory:', read_only=False)

# Define the first generator function
def people_1():
    for i in range(1, 6):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 25 + i, "City": "City_A"}

# Create a DuckDB table using the first generator
con.execute("CREATE TABLE people (ID INTEGER, Name VARCHAR, Age INTEGER, City VARCHAR)")
con.executemany("INSERT INTO people VALUES (?, ?, ?, ?)", list((person["ID"], person["Name"], person["Age"], person["City"]) for person in people_1()))

# Calculate the sum of ages for the first generator
result = con.execute("SELECT SUM(Age) FROM people")
print("Sum of ages of people from the first generator:", result.fetchone()[0])

# Define the second generator function
def people_2():
    for i in range(3, 9):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 30 + i, "City": "City_B", "Occupation": f"Job_{i}"}

# Append data from the second generator to the existing table
con.executemany("INSERT INTO people VALUES (?, ?, ?, ?)", list((person["ID"], person["Name"], person["Age"], person["City"]) for person in people_2()))

# Recalculate the sum of ages for all people in the combined table
result = con.execute("SELECT SUM(Age) FROM people")
print("Sum of ages of all people after appending the second generator data:", result.fetchone()[0])

# Close the connection to DuckDB
con.close()
```
#### Question 4
```
pip install duckdb
import duckdb

# Connect to DuckDB in-memory database
con = duckdb.connect(database=':memory:', read_only=False)

# Define the first generator function
def people_1():
    for i in range(1, 6):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 25 + i, "City": "City_A"}

# Define the second generator function
def people_2():
    for i in range(3, 9):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 30 + i, "City": "City_B", "Occupation": f"Job_{i}"}

# Create a dictionary to store the merged data using ID as the key
merged_data = {}

# Merge data from the first generator
for person in people_1():
    merged_data[person["ID"]] = person

# Merge data from the second generator
for person in people_2():
    merged_data[person["ID"]] = person

# Calculate the sum of ages
sum_of_ages = sum(person["Age"] for person in merged_data.values())
print("Sum of ages of all people after merging:", sum_of_ages)

# Close the connection to DuckDB
con.close()

```
