def generate_random_data(schema):
    """
    Generate random data for the given schema.
    """
    if isinstance(schema, StructType):
        return generate_struct(schema)

    elif isinstance(schema, ArrayType):
        return [generate_random_data(schema.elementType) for _ in range(random.randint(0, 5))]

    else:
        return generate_primitive(schema)


def generate_struct(schema):
    """
    Generate random StructType data for the given schema.
    """
    fields = []
    for field in schema.fields:
        name = field.name
        data_type = field.dataType
        value = generate_random_data(data_type)
        fields.append((name, value))
    return dict(fields)


def generate_primitive(schema):
    """
    Generate random primitive data for the given schema.
    """
    if isinstance(schema, StringType):
        return "string" + str(random.randint(1, 10))
    elif isinstance(schema, IntegerType):
        return random.randint(1, 100)
    elif isinstance(schema, LongType):
        return random.randint(1, 1000)
    elif isinstance(schema, DoubleType):
        return random.uniform(1, 10)
    elif isinstance(schema, FloatType):
        return random.uniform(1, 10)
    elif isinstance(schema, BooleanType):
        return bool(random.getrandbits(1))
    elif isinstance(schema, DateType):
        return str(random.randint(2000, 2023)) + "-" + str(random.randint(1, 12)) + "-" + str(random.randint(1, 28))
    else:
        return None
