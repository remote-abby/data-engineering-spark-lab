from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName('CustomerFilter').getOrCreate()

df = spark.read.csv('/app/datasets/ecommerce/customers.csv', header=True)
df.select(F.col('customer_id'), F.col('country'), F.col('signup_date')).show()
customer = df.filter(F.col('country')=='India').filter(F.col('signup_date')>'2024-05-01')
customer.select(F.col('customer_id'), F.col('country'), F.col('signup_date')).show()