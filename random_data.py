def generate_data(schema, df):
    """
    Generates random data for a given schema based on the min/max range in a Spark DataFrame.
    """
    table_data = []
    for field in schema.fields:
        field_name = field.name
        field_type = field.dataType
        if isinstance(field_type, StructType):
            struct_data = generate_struct(field_type)
            table_data.append(struct_data)
        else:
            col_min, col_max = df.selectExpr("min({})".format(field_name), "max({})".format(field_name)).first()
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
                col_max_time = datetime.datetime.strptime(col_max, "%Y-%m-%d %H:%M:%S")
                random_time = col_min_time + datetime.timedelta(seconds=random.randint(0, (col_max_time - col_min_time).total_seconds()))
                table_data.append(random_time)
            elif isinstance(field_type, ArrayType):
                array_data = [generate_random_data(field_type.elementType) for i in range(3)]
                table_data.append(array_data)
            elif isinstance(field_type, MapType):
                map_data = {generate_random_data(field_type.keyType): generate_random_data(field_type.valueType) for i in range(3)}
                table_data.append(map_data)
            else:
                table_data.append(None)
    return table_data
