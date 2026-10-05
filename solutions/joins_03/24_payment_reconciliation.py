from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder.appName("Reconcilition").getOrCreate()

orders = spark.read.csv('/app/datasets/ecommerce/orders.csv', header=True)
order_items = spark.read.csv('/app/datasets/ecommerce/order_items.csv', header=True)

orders = orders.filter(F.col('status')=='COMPLETED')
order_items = order_items.withColumn('total_amount_item', F.col('unit_price')*F.col('quantity')).groupby('order_id').agg(F.sum('total_amount_item').alias('order_total_calc'))

orders.join(order_items, on='order_id', how='inner').filter(F.col('order_total_calc')==F.col('total_amount')).show()
orders.join(order_items, on='order_id', how='inner').filter(F.col('order_total_calc')!=F.col('total_amount')).show()


