from pyspark.sql.types import *
from pyspark.sql.functions import udf, struct, array, col
from datetime import datetime, timedelta
import random

# Define a function to generate random data for each data type
def generate_random_data(data_type, nullable=True):
    if nullable and random.random() < 0.1:
        return None
    elif data_type == StringType():
        return ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 20)))
    elif data_type == IntegerType():
        return random.randint(-1000, 1000)
    elif data_type == LongType():
        return random.randint(-1000000, 1000000)
    elif data_type == FloatType():
        return random.uniform(-1000, 1000)
    elif data_type == DoubleType():
        return random.uniform(-1000000, 1000000)
    elif data_type == BooleanType():
        return random.choice([True, False])
    elif data_type == DateType():
        return datetime.today().date() + timedelta(days=random.randint(-365, 365))
    elif data_type == TimestampType():
        return datetime.now() + timedelta(seconds=random.randint(-3600, 3600))
    elif isinstance(data_type, ArrayType):
        inner_type = data_type.elementType
        return [generate_random_data(inner_type) for _ in range(random.randint(1, 10))]
    elif isinstance(data_type, StructType):
        fields = data_type.fields
        values = [generate_random_data(field.dataType) for field in fields]
        return struct(*values)
    else:
        raise ValueError(f"Unsupported data type: {data_type}")

# Define a function to generate random data for each column in the DataFrame
def generate_random_dataframe(df):
    struct_fields = [field for field in df.schema.fields if isinstance(field.dataType, StructType)]
    array_fields = [field for field in df.schema.fields if isinstance(field.dataType, ArrayType) and not isinstance(field.dataType.elementType, StructType)]

    # Define a UDF to generate random data for each row in the DataFrame
    random_data_udf = udf(lambda _: struct(*[generate_random_data(field.dataType) for field in df.schema.fields]), df.schema)

    # Apply the UDF to generate random data for each row in the DataFrame
    random_df = df.select(random_data_udf(col("*")).alias("random_data"))

    # Explode the struct fields to create columns for each field in the struct
    for field in struct_fields:
        random_df = random_df.selectExpr("random_data.*")

    # Explode the array fields to create a column for each element in the array
    for field in array_fields:
        random_df = random_df.withColumn(field.name, col(field.name).getItem(0))

    return random_df
