from pyspark.sql.types import *

def generate_random_data(schema, num_rows):
    # Create empty list to hold rows of data
    data = []

    # Generate data for each row
    for i in range(num_rows):
        # Create empty dictionary to hold data for this row
        row_data = {}

        # Generate data for each column
        for field in schema.fields:
            # Get column name and data type
            col_name = field.name
            data_type = field.dataType

            # Generate random data based on data type
            if isinstance(data_type, StructType):
                # Recursively generate random data for nested structs
                col_data = generate_random_data(data_type, 1)[0]
            elif isinstance(data_type, IntegerType):
                col_data = randint(0, 100)
            elif isinstance(data_type, LongType):
                col_data = randint(0, 100000)
            elif isinstance(data_type, StringType):
                col_data = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            elif isinstance(data_type, BooleanType):
                col_data = bool(random.getrandbits(1))
            elif isinstance(data_type, FloatType):
                col_data = random.uniform(0, 1)
            elif isinstance(data_type, DoubleType):
                col_data = random.uniform(0, 1)
            elif isinstance(data_type, DateType):
                col_data = datetime.date.today() - datetime.timedelta(days=randint(0, 365))
            else:
                raise Exception(f"Data type {data_type} not supported")

            # Add generated data to row dictionary
            row_data[col_name] = col_data

        # Add row dictionary to data list
        data.append(row_data)

    # Return data as Spark DataFrame
    return spark.createDataFrame(data, schema)
