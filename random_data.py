from pyspark.sql import SparkSession
from pyspark.sql.functions import rand, expr
from pyspark.sql.types import *

# Define a function to generate random data for each column type
def generate_random_data(data_type):
    if isinstance(data_type, StructType):
        return expr("struct(" + ",".join([generate_random_data(field.dataType) for field in data_type.fields]) + ")")
    elif isinstance(data_type, ArrayType):
        return expr("array(" + generate_random_data(data_type.elementType) + ")")
    elif isinstance(data_type, MapType):
        return expr("map_from_arrays(array(" + generate_random_data(data_type.keyType) + "), array(" + generate_random_data(data_type.valueType) + "))")
    elif isinstance(data_type, StringType):
        return expr("concat('string_', cast(rand() * 1000000000 as bigint))")
    elif isinstance(data_type, IntegerType):
        return expr("cast(rand() * 1000000000 as int)")
    elif isinstance(data_type, LongType):
        return expr("cast(rand() * 1000000000000000000 as bigint)")
    elif isinstance(data_type, FloatType):
        return expr("rand()")
    elif isinstance(data_type, DoubleType):
        return expr("rand() * 1000000")
    elif isinstance(data_type, DecimalType):
        return expr("cast(rand() * 1000000 as decimal(10, 2))")
    elif isinstance(data_type, TimestampType):
        return expr("date_add(to_utc_timestamp('1970-01-01', 'UTC'), cast(rand() * 1000000000 as bigint))")
    elif isinstance(data_type, DateType):
        return expr("date_add(to_date('1970-01-01'), cast(rand() * 10000 as int))")
    else:
        return expr("null")

# Create a SparkSession
spark = SparkSession.builder \
    .appName("RandomSampleDataGenerator") \
    .enableHiveSupport() \
    .getOrCreate()

# Read 100 rows from the Hive table
df = spark.sql("SELECT * FROM my_hive_table LIMIT 100")

# Generate random sample data based on the schema of the DataFrame
sample_df = df.select([generate_random_data(field.dataType).alias(field.name) for field in df.schema.fields])

# Show the sample data
sample_df.show()
