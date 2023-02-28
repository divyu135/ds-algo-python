from pyspark.sql.functions import rand, randn
from pyspark.sql import SparkSession

# create spark session
spark = SparkSession.builder.appName("RandomDataGenerator").getOrCreate()

# get column names from schema
column_names = [field.name for field in table_schema.fields]

# generate random data
df = spark.range(1000)
for column in column_names:
    df = df.withColumn(column, rand())

# create dataframe with correct schema
df = spark.createDataFrame(df.rdd, schema=table_schema)

# show dataframe
df.show()
