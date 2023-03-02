import random
from pyspark.sql.functions import explode, col, rand

# Define a PySpark DataFrame
df = ...

# Define a function to generate random values based on min and max values of a column
def generate_random_value(min_val, max_val, data_type):
    if data_type == "integer":
        return random.randint(min_val, max_val)
    elif data_type == "double":
        return round(random.uniform(min_val, max_val), 2)
    elif data_type == "boolean":
        return random.choice([True, False])
    elif data_type == "string":
        return ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(min_val, max_val)))
    elif data_type == "date":
        return (datetime.date.today() - datetime.timedelta(days=random.randint(min_val, max_val))).strftime('%Y-%m-%d')
    else:
        return None

# Define a function to unnest complex types and generate random values
def generate_random_row(row):
    for col_name, data_type in row.dtypes:
        if "struct" in data_type:
            for field_name, field_type in row.select(col(col_name + ".*")).schema.fields:
                min_val, max_val = row.select(col_name + "." + field_name).agg({"*": "min"}, {"*": "max"}).first()
                row[col_name + "_" + field_name] = generate_random_value(min_val, max_val, field_type.typeName())
            row = row.drop(col_name)
        elif "array" in data_type:
            row = row.withColumn(col_name, explode(col(col_name)))
        elif "map" in data_type:
            pass # handle map type here
        else:
            min_val, max_val = row.agg({col_name: "min"}, {col_name: "max"}).first()
            row[col_name] = generate_random_value(min_val, max_val, data_type)
    return row

# Generate 10 random rows of data
result = df.sample(False, 0.1, seed=42).limit(10).\
    select("*").\
    selectExpr("*", "rand() as random").\
    orderBy("random").\
    drop("random").\
    rdd.map(generate_random_row).toDF()
    
result.show()
