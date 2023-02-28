import random
import string
import datetime
import decimal

from pyspark.sql.functions import col
from pyspark.sql.types import StructType, ArrayType

# Define function to check if a string represents an integer
def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# Define function to get the distinct characters in a string column
def get_character_range(df, column):
    distinct_chars = set()
    for row in df.select(column).distinct().collect():
        if row[column] is not None:
            distinct_chars.update(list(row[column]))
    if len(distinct_chars) > 0:
        min_char = ord(min(distinct_chars))
        max_char = ord(max(distinct_chars))
        return (min_char, max_char)
    else:
        return None

# Define function to handle nested struct columns
def generate_sample_data_for_struct(df, column):
    # Get schema of the struct column
    struct_schema = df.schema[column].dataType
    # Generate sample data for each field in the struct
    sample_data = {}
    for field in struct_schema.fields:
        field_name = "{}.{}".format(column, field.name)
        if isinstance(field.dataType, StructType):
            # If field is nested struct, recursively generate sample data
            sample_data[field_name] = generate_sample_data_for_struct(df, field_name)
        elif isinstance(field.dataType, ArrayType):
            # If field is array, generate a random array of random length
            array_len = random.randint(1, 5)
            array_data = []
            for _ in range(array_len):
                array_data.append(generate_sample_data_for_type(df, field_name))
            sample_data[field_name] = array_data
        else:
            # Otherwise, generate sample data for the field
            sample_data[field_name] = generate_sample_data_for_type(df, field_name)
    return sample_data

# Define function to generate sample data for a given column type
def generate_sample_data_for_type(df, column):
    # Get range of column values
    column_ranges = {}
    character_ranges = {}
    for col_type in df.schema[column].dataType:
        if isinstance(col_type, StructType):
            # If column is struct, recursively generate sample data for each field in the struct
            column_ranges[column] = generate_sample_data_for_struct(df, column)
        elif isinstance(col_type, ArrayType):
            # If column is array, generate a random array of random length
            array_len = random.randint(1, 5)
            array_data = []
            for _ in range(array_len):
                array_data.append(generate_sample_data_for_type(df, column))
            column_ranges[column] = array_data
        elif isinstance(col_type, str):
            # If column is string, get range of string lengths
            min_len = df.agg({column: "min"}).collect()[0][0]
            max_len = df.agg({column: "max"}).collect()[0][0]
            column_ranges[column] = (min_len, max_len)
            # If column has a range of characters, get range of character values
            char_range = get_character_range(df, column)
            if char_range is not None:
                character_ranges[column] = char_range
        elif isinstance(col_type, (datetime.date, datetime.datetime)):
            # If column is date or datetime, get range of dates/times
            column_ranges[column] = (df.agg({"{}".format(column): "min"}).collect()[0][0], df.agg({"{}".format(column): "max"}).collect()[0][0])
        elif isinstance(col_type, decimal.Decimal):
            # If column is decimal, get range of decimal values
            column_ranges[column] = (float(df.agg({"{}".format(column): "min"}).collect()[0][0]), float(df.agg({"{}".format(column): "max"}).collect()[0][0]))
        elif isinstance(col_type, bool):
            # If column is boolean, generate a random boolean value
            column_ranges[column] = (False, True)
        elif isinstance(col_type, (int, float)):
            # If column is numeric, get range of numeric values
            column_ranges[column] = (df.agg({"{}".format(column): "min"}).collect()[0][0], df.agg({"{}".format(column): "max"}).collect()[0][0])

    # Generate sample data based on column type and range
    sample_data = None
    for col_type in df.schema[column].dataType:
        if isinstance(col_type, StructType):
            # If column is struct, recursively generate sample data for each field in the struct
            sample_data = generate_sample_data_for_struct(df, column)
        elif isinstance(col_type, ArrayType):
            # If column is array, generate a random array of random length
            array_len = random.randint(1, 5)
            array_data = []
            for _ in range(array_len):
                array_data.append(generate_sample_data_for_type(df, column))
            sample_data = array_data
        elif isinstance(col_type, str):
            # If column is string, generate a random string of random length and characters
            if column in character_ranges:
                # If column has a range of characters, generate random string within that range
                min_char, max_char = character_ranges[column]
                length = random.randint(*column_ranges[column])
                sample_data = "".join([chr(random.randint(min_char, max_char)) for _ in range(length)])
            else:
                # If column does not have a range of characters, generate random string with alphanumeric characters
                length = random.randint(*column_ranges[column])
                sample_data = "".join([random.choice(string.ascii_letters + string.digits) for _ in range(length)])
        elif isinstance(col_type, (datetime.date, datetime.datetime)):
            # If column is date or datetime, generate a random date/time within the range
            min_date, max_date = column_ranges[column]
            delta = max_date - min_date
            random_date = min_date + datetime.timedelta(seconds=random.randint(0, delta.total_seconds()))
            sample_data = random_date
        elif isinstance(col_type, decimal.Decimal):
            # If column is decimal, generate a random decimal value within the range
            min_val, max_val = column_ranges[column]
            decimal_places = col_type.as_tuple().exponent * -1
            sample_data = round(random.uniform(min_val, max_val), decimal_places)
        elif isinstance(col_type, bool):
            # If column is boolean, generate a random boolean value
            sample_data = random.choice([False, True])
        elif isinstance(col_type, (int, float)):
            # If column is numeric, generate a random value within the range
            sample_data = random.uniform(*column_ranges[column])
            if col_type == int:
                sample_data = int(sample_data)
    
    return sample_data
