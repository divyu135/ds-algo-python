def get_min_max(df, field_name):
    """
    Returns the minimum and maximum values for a given column in a Spark DataFrame.
    """
    col_min, col_max = df.selectExpr("min({})".format(field_name), "max({})".format(field_name)).first()
    if col_min is None or col_max is None:
        return None, None
    return col_min, col_max

def get_field_min_max(df, field, parent_name=None):
    """
    Recursively gets the minimum and maximum values for a field in a StructType schema.
    """
    field_name = field.name
    field_type = field.dataType
    full_field_name = field_name if parent_name is None else parent_name + "." + field_name
    if isinstance(field_type, StructType):
        min_max_values = {}
        for sub_field in field_type.fields:
            sub_min_max_values = get_field_min_max(df, sub_field, full_field_name)
            min_max_values.update(sub_min_max_values)
        return min_max_values
    else:
        col_min, col_max = get_min_max(df, full_field_name)
        return {full_field_name: (col_min, col_max)}

def get_schema_min_max(df, schema):
    """
    Gets the minimum and maximum values for all fields in a StructType schema.
    """
    schema_min_max = {}
    for field in schema.fields:
        field_min_max = get_field_min_max(df, field)
        schema_min_max.update(field_min_max)
    return schema_min_max

def generate_data(schema, df):
    """
    Generates random data for a given schema based on the min/max range in a Spark DataFrame.
    """
    schema_min_max = get_schema_min_max(df, schema)
    table_data = []
    for field in schema.fields:
        field_name = field.name
        field_type = field.dataType
        if isinstance(field_type, StructType):
            struct_data = generate_struct(field_type, schema_min_max)
            table_data.append(struct_data)
        else:
            col_min, col_max = schema_min_max[field_name]
            if isinstance(field_type, StringType):
                table_data.append(''.join(random.choice(string.ascii_letters) for i in range(10)))
            elif isinstance(field_type, IntegerType):
                table_data.append(random.randint(col_min, col_max))
            elif isinstance(field_type, LongType):
                table_data.append(random.randint(col_min, col_max))
            elif isinstance(field_type, DoubleType):
                table_data.append(random.uniform(col_min, col_max))
            elif isinstance(field_type, BooleanType):
                table_data.append(random.choice([True, False]))
            elif isinstance(field_type, DateType):
                col_min_date = datetime.datetime.strptime(col_min, "%Y-%m-%d").date()
                col_max_date = datetime.datetime.strptime(col_max, "%Y-%m-%d").date()
                random_date = col_min_date + datetime.timedelta(days=random.randint(0, (col_max_date - col_min_date).days))
                table_data.append(random_date)
            elif isinstance(field_type, TimestampType):
                col_min_time = datetime.datetime.strptime(col_min, "%Y-%m-%d %H:%M:%S")
                col_max_time = datetime.datetime.strptime(col_max, "%Y-%m-%d %H:%
