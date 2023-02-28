from pyspark.sql import SparkSession
from pyspark.sql.functions import rand, expr
from pyspark.sql.types import *

# Define a function to generate random data for each column type
def generate_random_data(data_type):
    if isinstance(data_type, StructType):
        fields_expr = [generate_random_data(field.dataType).alias(field.name) for field in data_type.fields]
        return expr("struct(" + ",".join([f"`{f.name}`" for f in data_type.fields]) + ")").select(*fields_expr)
    elif isinstance(data_type, ArrayType):
        return expr("array(" + generate_random_data(data_type.elementType).cast("string") + ")")
    elif isinstance(data_type, MapType):
        key_expr = generate_random_data(data_type.keyType).cast("string")
        value_expr = generate_random_data(data_type.valueType).cast("string")
        return expr("map_from_arrays(array(" + key_expr + "), array(" + value_expr + "))")
    elif isinstance(data_type, StringType):
        return expr("concat('string_', cast(rand() * 100 as int))")
    elif isinstance(data_type, IntegerType):
        return expr("cast(rand() * 100 as int)")
    elif isinstance(data_type, DoubleType):
        return expr("rand()")
    elif isinstance(data_type, BooleanType):
        return expr("(rand() > 0.5)")
    elif isinstance(data_type, TimestampType):
        return expr("from_unixtime(rand() * 1000000000)")
    elif isinstance(data_type, DateType):
        return expr("from_unixtime(rand() * 1000000000, 'yyyy-MM-dd')").cast("date")
    else:
        raise ValueError(f"Unsupported data type: {data_type}")

# Create a SparkSession
spark = SparkSession.builder \
    .appName("Generate random data for a Hive table") \
    .enableHiveSupport() \
    .getOrCreate()

# Define the name of the Hive table
table_name = "my_table"

# Load the schema of the Hive table
table_schema = spark.table(table_name).schema

# Get 100 rows from the Hive table and store them in a DataFrame
df = spark.sql(f"SELECT * FROM {table_name} LIMIT 100")

# Generate random data for each column based on its data type
random_exprs = [generate_random_data(field.dataType).alias(field.name) for field in table_schema.fields]

# Add the random data to the DataFrame
df_with_random_data = df.select(*random_exprs)

# Show the first 10 rows of the DataFrame
df_with_random_data.show(10)
