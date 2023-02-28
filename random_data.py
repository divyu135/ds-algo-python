import random
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType, DoubleType, IntegerType, LongType, DecimalType, FloatType, DateType, TimestampType, StructType, ArrayType, StructField

# Define a function to generate random data based on column data type
def generate_random_data(col_type, col_range=None):
    if col_type == StringType():
        return ''.join(random.choices(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], k=random.randint(5, 10)))
    elif col_type == DoubleType() or col_type == FloatType() or col_type == DecimalType():
        return random.uniform(col_range[0], col_range[1])
    elif col_type == IntegerType() or col_type == LongType():
        return random.randint(col_range[0], col_range[1])
    elif col_type == DateType():
        return str(random.randint(col_range[0], col_range[1]))
    elif col_type == TimestampType():
        return str(random.randint(col_range[0], col_range[1]))
    else:
        return None

# Define a function to recursively generate random data for struct and array types
def generate_random_data_for_complex_types(col_type, col_range=None):
    if isinstance(col_type, StructType):
        return [generate_random_data_for_complex_types(f.dataType, None) for f in col_type.fields]
    elif isinstance(col_type, ArrayType):
        return [generate_random_data_for_complex_types(col_type.elementType, None)]
    else:
        return generate_random_data(col_type, col_range)

# Define a UDF to generate random data for each column based on column data type and range
generate_random_data_udf = udf(generate_random_data_for_complex_types, StructType([
    StructField("col", StructType([
        StructField("type", StringType(), True),
        StructField("data", col.dataType, True)
    ]), True)
]))

# Create a list of StructFields representing the columns of the DataFrame with their data type
cols = [StructField(c.name, StructType([
    StructField("type", StringType(), True),
    StructField("data", c.dataType, True)
]), True) for c in df.schema]

# Create a new DataFrame with the same schema as the original, but with the data replaced by random data
dummy_df = df.select([generate_random_data_udf(
    StructType([cols[i]]).alias(cols[i].name)
).alias(cols[i].name) for i in range(len(cols))])
