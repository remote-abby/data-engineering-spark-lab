from pyspark.sql import SparkSession, functions as F, window

spark = SparkSession.builder.appName("largestOrder").getOrCreate()

orders = spark.read.csv('/app/datasets/ecommerce/orders.csv', header=True)
customers = spark.read.csv('/app/datasets/ecommerce/customers.csv', header=True)

cust_ord = customers.join(orders, on='customer_id', how='inner')
globwin = window.Window.partitionBy()

cust_ord.withColumn("maxAmount", F.max(F.col('total_amount')).over(globwin)).filter((F.col('total_amount')==F.col('maxAmount')) & (F.col('status')=='COMPLETED')).show()