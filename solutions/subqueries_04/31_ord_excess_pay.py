from pyspark.sql import SparkSession, functions as F, window

spark = SparkSession.builder.appName("excessPay").getOrCreate()

orders = spark.read.csv('/app/datasets/ecommerce/orders.csv', header=True)
order_items = spark.read.csv('/app/datasets/ecommerce/order_items.csv', header=True)

orders = orders.filter(F.col('status')=='COMPLETED')
order_details = order_items.join(orders, on='order_id', how='inner').withColumn("item_total_cost", F.col('quantity')*F.col('unit_price'))
order_details.groupby('order_id', 'total_amount').agg(F.sum('item_total_cost').alias('exp_total_cost')).filter(F.col('total_amount')>F.col('exp_total_cost')).show()