
### Data Warehousing and Big Query

* This topic covers the Data Warehousing concepts, using BigQuery and the basics of partitioning and clustering.

* Advanced topics include BigQuery internals, machine learning

#### Answers to Questions

Dataset located here: https://console.cloud.google.com/bigquery?project=calcium-alchemy-256812&ws=!1m5!1m4!4m3!1scalcium-alchemy-256812!2sTaxi!3scombined_taxi_data 

* Question 1. Question 1: What is count of records for the 2022 Green Taxi Data?

Query: `SELECT count (*) FROM calcium-alchemy-256812.Taxi.combined_taxi_data` 

* Question 2. Write a query to count the distinct number of PULocationIDs for the entire dataset on both the tables.
What is the estimated amount of data that will be read when this query is executed on the External Table and the Table?

Query: `SELECT COUNT(DISTINCT PULocationID) AS distinct_PULocationIDs FROM calcium-alchemy-256812.Taxi.combined_taxi_data`

* Question 3. How many records have a fare_amount of 0?

Query: `SELECT COUNT(fare_amount) FROM calcium-alchemy-256812.Taxi.combined_taxi_data where fare_amount = 0`

* Question 4. What is the best strategy to make an optimized table in Big Query if your query will always order the results by PUlocationID and filter based on lpep_pickup_datetime? (Create a new table with this strategy)

(Answer on form)

* Question 5. Write a query to retrieve the distinct PULocationID between lpep_pickup_datetime 06/01/2022 and 06/30/2022 (inclusive)

Use the materialized table you created earlier in your from clause and note the estimated bytes. Now change the table in the from clause to the partitioned table you created for question 4 and note the estimated bytes processed. What are these values?
```
-- Query using the materialized table
SELECT COUNT(DISTINCT PULocationID) AS distinct_PULocationIDs_materialized
FROM calcium-alchemy-256812.Taxi.combined_taxi_data
WHERE lpep_pickup_datetime BETWEEN TIMESTAMP('2022-06-01') AND TIMESTAMP('2022-06-30')

-- Query using the partitioned table
SELECT COUNT(DISTINCT PULocationID) AS distinct_PULocationIDs_partitioned
FROM calcium-alchemy-256812.Taxi.combined_taxi_data
WHERE lpep_pickup_datetime BETWEEN TIMESTAMP('2022-06-01') AND TIMESTAMP('2022-06-30')
```
* Question 6. Where is the data stored in the External Table you created?

(Answer on form)

* Question 7. It is best practice in Big Query to always cluster your data

(Answer on form)



