from pyspark.sql import functions as F

def clean_data(df):
    df_cleaned = df.filter((F.col("amount") > 0) & (F.col("name").isNotNull()))

    df_cleaned = df_cleaned.withColumn("amount_with_tax", F.col("amount") * 1.20)

    return df_cleaned
