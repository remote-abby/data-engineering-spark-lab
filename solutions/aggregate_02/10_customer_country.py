from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("customerCountry").getOrCreate()

df = spark.read.csv('/app/datasets/ecommerce/customers.csv', header=True)

df.groupby(F.col('country')).agg(F.count('*').alias('customer_count')).show()