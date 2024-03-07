from pyspark.sql import SparkSession

# Create a local Spark session
spark = SparkSession.builder \
    .appName("SparkVersionTest") \
    .master("local[*]") \
    .getOrCreate()

# Get the Spark version
spark_version = spark.version

# Print the Spark version
print("Spark version:", spark_version)
