# Step 1: Import SparkSession
from pyspark.sql import SparkSession

# Step 2: Create SparkSession
spark = SparkSession.builder \
    .appName("SampleSparkApp") \
    .getOrCreate()

# Step 3: Create sample data
data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
columns = ["Name", "Age"]

# Step 4: Create DataFrame
df = spark.createDataFrame(data, columns)

# Step 5: Show DataFrame
df.show()

# Step 6: Perform basic operations
df.select("Name").show()
df.filter(df.Age > 28).show()
df.groupBy("Age").count().show()

# Step 7: Stop SparkSession
spark.stop()
