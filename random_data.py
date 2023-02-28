from pyspark.sql.functions import udf, expr
from pyspark.sql.types import *

def generate_random_data(data_type):
    if isinstance(data_type, StringType):
        return udf(lambda: "test string")()
    elif isinstance(data_type, IntegerType):
        return udf(lambda: 1)()
    elif isinstance(data_type, LongType):
        return udf(lambda: 1)()
    elif isinstance(data_type, FloatType):
        return udf(lambda: 1.0)()
    elif isinstance(data_type, DoubleType):
        return udf(lambda: 1.0)()
    elif isinstance(data_type, BooleanType):
        return udf(lambda: True)()
    elif isinstance(data_type, DateType):
        return udf(lambda: "2022-01-01")()
    elif isinstance(data_type, TimestampType):
        return udf(lambda: "2022-01-01 00:00:00")()
    elif isinstance(data_type, DecimalType):
        return udf(lambda: Decimal(1))()
    elif isinstance(data_type, ArrayType):
        return udf(lambda: [generate_random_data(data_type.elementType) for i in range(3)])()
    elif isinstance(data_type, MapType):
        return udf(lambda: {"key": generate_random_data(data_type.keyType), "value": generate_random_data(data_type.valueType)})()
    elif isinstance(data_type, StructType):
        fields_expr = [expr("`" + f.name + "`") for f in data_type.fields]
        return expr("struct(" + ",".join([generate_random_data(field.dataType) for field in data_type.fields]) + ")").select(*fields_expr)
    elif isinstance(data_type, NullType):
        return udf(lambda: None)()
    else:
        raise ValueError("Unsupported data type: " + str(data_type))


from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("Generate Random Data").enableHiveSupport().getOrCreate()

# Read the schema of the Hive table
table_schema = spark.table("<database_name>.<table_name>").schema

# Generate random data based on the schema
random_data = generate_random_data(table_schema)

# Show the generated data
random_data.show()
