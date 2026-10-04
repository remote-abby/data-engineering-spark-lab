from pyspark.sql import SparkSession, functions as F, window

spark = SparkSession.builder.appName("RevCat").getOrCreate()

orders = spark.read.csv('/app/datasets/ecommerce/orders.csv', header=True)
order_items = spark.read.csv('/app/datasets/ecommerce/order_items.csv', header=True)
products = spark.read.csv('/app/datasets/ecommerce/products.csv', header=True)

comp_orders = orders.join(order_items, on='order_id', how='inner').filter(F.col('status')=='COMPLETED')
comp_order = comp_orders.withColumn("item_total_amount", F.col('quantity')*F.col('unit_price'))
cat_rev = comp_order.join(products, on='product_id', how='inner').groupby('category').agg(F.sum('item_total_amount').alias('cat_revenue'))

globwin = window.Window.partitionBy()
cat_rev.withColumn("rev%", F.concat( F.round(F.col('cat_revenue')*100 / F.sum(F.col('cat_revenue')).over(globwin),2), F.lit('%'))).show()