from pyspark.sql import SparkSession, functions as F, window

spark = SparkSession.builder.appName("MulPayMethod").getOrCreate()

payments = spark.read.csv('/app/datasets/ecommerce/payments.csv', header=True)
orders = spark.read.csv('/app/datasets/ecommerce/orders.csv', header=True)
globwin = window.Window.partitionBy()
payments.join(orders, on='order_id', how='inner').groupby('order_id').agg(F.count_distinct(F.col('payment_method')).alias('dist_methods')).filter(F.col('dist_methods')>1).show()
