from pyspark.sql.types import *
import random
import string
import datetime

def generate_struct(schema, df):
    """
    Generates random data for a StructType schema based on the min/max range in a Spark DataFrame.
    """
    struct_data = {}
    for field in schema.fields:
        field_name = field.name
        field_type = field.dataType
        if isinstance(field_type, StructType):
            struct_data[field_name] = generate_struct(field_type, df)
        else:
            col_min, col_max = df.selectExpr("min({})".format(field_name), "max({})".format(field_name)).first()
            struct_data[field_name] = generate_random_data(field_type, col_min, col_max)
    return struct_data

def generate_random_data(data_type, col_min, col_max):
    """
    Generates random data for a given data type based on the min/max range.
    """
    if isinstance(data_type, StringType):
        return ''.join(random.choice(string.ascii_letters) for i in range(10))
    elif isinstance(data_type, IntegerType):
        return random.randint(col_min, col_max)
    elif isinstance(data_type, LongType):
        return random.randint(col_min, col_max)
    elif isinstance(data_type, DoubleType):
        return random.uniform(col_min, col_max)
    elif isinstance(data_type, BooleanType):
        return random.choice([True, False])
    elif isinstance(data_type, DateType):
        col_min_date = datetime.datetime.strptime(col_min, "%Y-%m-%d").date()
        col_max_date = datetime.datetime.strptime(col_max, "%Y-%m-%d").date()
        random_date = col_min_date + datetime.timedelta(days=random.randint(0, (col_max_date - col_min_date).days))
        return random_date
    elif isinstance(data_type, TimestampType):
        col_min_time = datetime.datetime.strptime(col_min, "%Y-%m-%d %H:%M:%S")
        col_max_time = datetime.datetime.strptime(col_max, "%Y-%m-%d %H:%M:%S")
        random_time = col_min_time + datetime.timedelta(seconds=random.randint(0, (col_max_time - col_min_time).total_seconds()))
        return random_time
    elif isinstance(data_type, ArrayType):
        return [generate_random_data(data_type.elementType, col_min, col_max) for i in range(3)]
    elif isinstance(data_type, MapType):
        return {generate_random_data(data_type.keyType, col_min, col_max): generate_random_data(data_type.valueType, col_min, col_max) for i in range(3)}
    else:
        return None

def generate_data(schema, df):
    """
    Generates random data for a given schema based on the min/max range in a Spark DataFrame.
    """
    table_data = []
    for field in schema.fields:
        field_name = field.name
        field_type = field.dataType
        if isinstance(field_type, StructType):
            struct_data = generate_struct(field_type, df)
            table_data.append(struct_data)
        else:
            col_min, col_max = df.selectExpr("min({})".format(field_name), "max({})".format(field_name)).first()
            table_data.append(generate_random_data(field_type, col_min, col_max))
    return table_data
