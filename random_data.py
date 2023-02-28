import random
import string
import datetime
import decimal
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, ArrayType


def get_table_column_ranges(spark, table_name):
    df = spark.table(table_name)
    column_ranges = {}
    for column in df.columns:
        column_type = df.schema[column].dataType
        if isinstance(column_type, (int, float, decimal.Decimal)):
            column_ranges[column] = (df.agg({column: "min"}).collect()[0][0], df.agg({column: "max"}).collect()[0][0])
        elif isinstance(column_type, str):
            distinct_vals = df.select(column).distinct().rdd.map(lambda r: r[0]).collect()
            if len(distinct_vals) == 1:
                column_ranges[column] = len(distinct_vals[0])
            elif all(val.isdigit() for val in distinct_vals):
                column_ranges[column] = (min(int(val) for val in distinct_vals), max(int(val) for val in distinct_vals))
            elif all(len(val) == 1 for val in distinct_vals):
                column_ranges[column] = (min(ord(val) for val in distinct_vals), max(ord(val) for val in distinct_vals))
            else:
                column_ranges[column] = None
        elif isinstance(column_type, (datetime.date, datetime.datetime)):
            column_ranges[column] = (df.agg({column: "min"}).collect()[0][0], df.agg({column: "max"}).collect()[0][0])
        elif isinstance(column_type, bool):
            column_ranges[column] = None
        elif isinstance(column_type, StructType):
            column_ranges[column] = get_struct_column_ranges(column_type)
        elif isinstance(column_type, ArrayType) and isinstance(column_type.elementType, StructType):
            column_ranges[column] = [get_struct_column_ranges(column_type.elementType)]
        else:
            column_ranges[column] = None
    return column_ranges


def get_struct_column_ranges(struct_type):
    struct_ranges = {}
    for field in struct_type.fields:
        field_type = field.dataType
        if isinstance(field_type, StructType):
            struct_ranges[field.name] = get_struct_column_ranges(field_type)
        elif isinstance(field_type, ArrayType) and isinstance(field_type.elementType, StructType):
            struct_ranges[field.name] = [get_struct_column_ranges(field_type.elementType)]
        else:
            struct_ranges[field.name] = (None, None)
    return struct_ranges


def generate_sample_data_for_type(col_type, column_ranges):
    if isinstance(col_type, (int, float, decimal.Decimal)):
        return random.uniform(column_ranges[0], column_ranges[1])
    elif isinstance(col_type, str):
        if is_character_range(column_ranges):
            return "".join(random.choices(string.ascii_letters + string.digits, k=column_ranges))
        elif isinstance(column_ranges, tuple) and all(isinstance(val, int) for val in column_ranges):
            return str(random.randint(column_ranges[0], column_ranges[1]))
        else:
            return None
    elif isinstance(col_type, (datetime.date, datetime.datetime)):
        epoch_start = col_type.fromisoformat('1970-01-01')
        start_seconds = (column_ranges[0] - epoch_start).total_seconds()
        end_seconds = (column_ranges[1] - epoch_start).total_seconds()
        return datetime.datetime.fromtimestamp(random.uniform(start_seconds, end_seconds)).isoformat()
    elif isinstance(col_type, bool):
        return random.choice([True, False])
    elif isinstance(col_type, StructType):
        return {field.name: generate



from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder.appName("Generate Sample Data").getOrCreate()

# Specify Hive table name
table_name = "mytable"

# Get column ranges for table
column_ranges = get_table_column_ranges(spark, table_name)

# Generate sample data for each column
sample_data = {}
for col_name, col_range in column_ranges.items():
    sample_data[col_name] = generate_sample_data_for_type(col_range)

# Print sample data
for col_name, col_data in sample_data.items():
    print(f"{col_name}: {col_data}")
