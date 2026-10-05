from pyspark.sql import SparkSession, functions as F, window

spark = SparkSession.builder.appName("MulPayMethod").getOrCreate()

customers = spark.read.csv('/app/datasets/ecommerce/customers.csv', header=True)
orders = spark.read.csv('/app/datasets/ecommerce/orders.csv', header=True)

df = customers.join( orders, on='customer_id', how='left')
df.show()
