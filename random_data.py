from pyspark.sql.functions import rand, col, udf
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType, DateType, TimestampType

def generate_random_value(min_val, max_val, data_type):
    """
    Helper function to generate a random value based on a given data type and its min/max range.
    """
    if data_type == IntegerType():
        return int(rand() * (max_val - min_val + 1) + min_val)
    elif data_type == FloatType():
        return rand() * (max_val - min_val) + min_val
    elif data_type == StringType():
        return ''.join([chr(int(rand() * 26) + 97) for i in range(max_val)])  # generate a random string of lowercase letters
    elif data_type == DateType():
        return datetime.date.fromordinal(int(rand() * (max_val - min_val + 1)) + min_val)
    elif data_type == TimestampType():
        return datetime.datetime.fromordinal(int(rand() * (max_val - min_val + 1)) + min_val)
    else:
        raise ValueError(f"Unsupported data type: {data_type}")

def generate_random_data(df, num_rows=10):
    """
    Generates random data for a PySpark dataframe.
    """
    # Define a UDF to generate a random value for each primitive type column
    generate_random_udf = udf(lambda min_val, max_val, data_type: generate_random_value(min_val, max_val, data_type))

    # Loop through each column in the dataframe and generate a random value for each primitive type column
    for col_name, data_type in df.dtypes:
        if isinstance(data_type, StructType):
            generate_random_data(df.withColumnRenamed(col_name, col_name + "_temp"), num_rows)  # recursive call to handle nested structs
            df = df.drop(col_name).withColumn(col_name, col(col_name + "_temp")).drop(col_name + "_temp")
        else:
            # Calculate the min and max values for the current column
            col_min = df.selectExpr(f"min({col_name})").collect()[0][0]
            col_max = df.selectExpr(f"max({col_name})").collect()[0][0]

            # Generate a random value for the current column and overwrite the existing values in the dataframe
            random_values = [generate_random_udf(col(f"'{col_min}'"), col(f"'{col_max}'"), col(f"CAST('{data_type}' AS STRING)")).alias(col_name) for i in range(num_rows)]
            df = df.limit(num_rows).select(random_values)

    return df
