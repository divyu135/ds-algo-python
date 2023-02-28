from pyspark.sql.functions import rand, randn
from pyspark.sql import SparkSession

# create spark session
spark = SparkSession.builder.appName("RandomDataGenerator").getOrCreate()

# function to generate random data for each field
def generate_random_data(data_type):
    if data_type == "string":
        return rand()
    elif data_type == "integer":
        return (rand() * 1000).cast("integer")
    elif data_type == "long":
        return (rand() * 1000000000).cast("long")
    elif data_type == "date":
        return (rand() * 1000).cast("integer").cast("date")
    elif isinstance(data_type, StructType):
        return generate_random_struct(data_type)
    else:
        return None

# function to generate random data for struct type fields
def generate_random_struct(struct_type):
    struct_fields = struct_type.fields
    struct_dict = {}
    for field in struct_fields:
        field_name = field.name
        field_data_type = field.dataType
        field_data = generate_random_data(field_data_type)
        struct_dict[field_name] = field_data
    return struct_type(**struct_dict)

# get column names and data types from schema
column_names = [field.name for field in table_schema.fields]
column_data_types = [field.dataType for field in table_schema.fields]

# generate random data for each column
data = [generate_random_data(data_type) for data_type in column_data_types]

# create dataframe with correct schema
df = spark.createDataFrame([tuple(data)], schema=table_schema)

# show dataframe
df.show()
