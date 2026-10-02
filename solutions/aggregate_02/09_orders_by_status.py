
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("orderStatus").getOrCreate()

df = spark.read.csv('/app/datasets/ecommerce/orders.csv', header=True)
df.groupby(F.col('status')).agg(F.count('*').alias('status_count')).show()