from pyspark.sql import SparkSession, functions as F, window

spark = SparkSession.builder.appName("MulPayMethod").getOrCreate()

payments = spark.read.csv('/app/datasets/ecommerce/payments.csv', header=True)
orders = spark.read.csv('/app/datasets/ecommerce/orders.csv', header=True)
globwin = window.Window.partitionBy()
df = orders.join( payments, on='order_id', how='left')
df.show()
df.filter(F.col('payment_id').isNull()).select('order_id').show()
