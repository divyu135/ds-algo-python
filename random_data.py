from pyspark.sql.types import *

def generate_struct(schema):
    """
    Generates random data for a StructType schema.
    """
    struct_data = {}
    for field in schema.fields:
        field_name = field.name
        field_type = field.dataType
        if isinstance(field_type, StructType):
            struct_data[field_name] = generate_struct(field_type)
        else:
            struct_data[field_name] = generate_random_data(field_type)
    return struct_data

def generate_random_data(data_type):
    """
    Generates random data for a given data type.
    """
    if isinstance(data_type, StringType):
        return ''.join(random.choice(string.ascii_letters) for i in range(10))
    elif isinstance(data_type, IntegerType):
        return random.randint(0, 100)
    elif isinstance(data_type, LongType):
        return random.randint(0, 100000000)
    elif isinstance(data_type, DoubleType):
        return random.random() * 100
    elif isinstance(data_type, BooleanType):
        return random.choice([True, False])
    elif isinstance(data_type, DateType):
        return datetime.date.today() - datetime.timedelta(days=random.randint(0, 365))
    elif isinstance(data_type, TimestampType):
        return datetime.datetime.now() - datetime.timedelta(seconds=random.randint(0, 3600))
    elif isinstance(data_type, ArrayType):
        return [generate_random_data(data_type.elementType) for i in range(3)]
    elif isinstance(data_type, MapType):
        return {generate_random_data(data_type.keyType): generate_random_data(data_type.valueType) for i in range(3)}
    else:
        return None

def generate_data(schema):
    """
    Generates random data for a given schema.
    """
    table_data = []
    for field in schema.fields:
        field_name = field.name
        field_type = field.dataType
        if isinstance(field_type, StructType):
            struct_data = generate_struct(field_type)
            table_data.append(struct_data)
        else:
            table_data.append(generate_random_data(field_type))
    return table_data
