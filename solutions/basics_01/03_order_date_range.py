from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName('DateRange').getOrCreate()

df = spark.read.csv('/app/datasets/ecommerce/orders.csv', header=True)

# order_id,customer_id,
# order_date,status,
# total_amount
df.select(F.col('order_id'), F.col('order_date')).show()
feb_orders = df.filter(F.col('order_date').between('2024-02-01', '2024-02-31'))
feb_orders.select(F.col('order_id'), F.col('order_date')).show()
