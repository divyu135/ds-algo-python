from pyspark.sql.functions import rand, create_map, struct, size, col, lit, when
from pyspark.sql.types import StructType, StructField, IntegerType, DoubleType, StringType, ArrayType, MapType

# Define a sample PySpark DataFrame with different data types
df = spark.createDataFrame([(1, 2.0, "foo", [1, 2, 3], {'key1': 'value1', 'key2': 'value2'}, (4, "bar")),
                            (2, 3.0, "bar", [4, 5], {'key3': 'value3', 'key4': 'value4'}, (5, "baz"))],
                           ["col_int", "col_float", "col_string", "col_array", "col_map", "col_struct"])

# Define a function to generate random data based on the min-max range of a column
def generate_random_data(min_val, max_val, data_type):
    if isinstance(data_type, IntegerType):
        return int(rand() * (max_val - min_val) + min_val)
    elif isinstance(data_type, DoubleType):
        return rand() * (max_val - min_val) + min_val
    elif isinstance(data_type, StringType):
        return str(rand() * (max_val - min_val) + min_val)
    elif isinstance(data_type, ArrayType):
        return [generate_random_data(min_val, max_val, data_type.elementType) for _ in range(3)]
    elif isinstance(data_type, MapType):
        return create_map([lit(str(i)).alias("key"), generate_random_data(min_val, max_val, data_type.valueType).alias("value")] for i in range(2))
    elif isinstance(data_type, StructType):
        return struct([generate_random_data(min_val, max_val, field.dataType).alias(field.name) for field in data_type.fields])
    else:
        return None

# Generate random data for each column based on the min-max range of the DataFrame
df_min = df.agg(*(min(col(column)).alias(column) for column in df.columns))
df_max = df.agg(*(max(col(column)).alias(column) for column in df.columns))

min_values = df_min.first()
max_values = df_max.first()

random_data = [generate_random_data(min_val, max_val, data_type) for (min_val, max_val, data_type) in zip(min_values, max_values, df.schema.fields)]

# Create a new PySpark DataFrame with the generated random data
random_df = spark.createDataFrame([tuple(random_data)], schema=df.schema)

# Show the generated random data DataFrame
random_df.show()
