import pytest
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DoubleType
from pyspark_job import clean_data

@pytest.fixture(scope="session")
def spark():
    return SparkSession.builder.master("local").appName("PySpark-Testing").getOrCreate()

def test_clean_data(spark):
    schema = StructType([
        StructField("name", StringType(), True),
        StructField("amount", DoubleType(), True)
    ])
    
    data = [
        ("Ahmed", 100.0),    # سليم
        ("Mohamed", -5.0),   # مرفوض
        (None, 50.0),        # مرفوض
        ("Sara", 0.0)        # مرفوض
    ]
    
    df = spark.createDataFrame(data, schema)
    result_df = clean_data(df)
    results = result_df.collect()

    assert len(results) == 1
    assert results[0]["name"] == "Ahmed"
    assert results[0]["amount_with_tax"] == 120.0
