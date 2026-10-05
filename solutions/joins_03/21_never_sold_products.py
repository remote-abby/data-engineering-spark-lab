from pyspark.sql import SparkSession, functions as F, window

spark = SparkSession.builder.appName("MulPayMethod").getOrCreate()

products = spark.read.csv('/app/datasets/ecommerce/products.csv', header=True)
orders = spark.read.csv('/app/datasets/ecommerce/orders.csv', header=True)
order_items = spark.read.csv('/app/datasets/ecommerce/order_items.csv', header=True)

df = products.join( order_items, on='product_id', how='left')
df.show()
df = df.join(orders, on='order_id', how='left').filter(F.col('order_id').isNull()).select('product_id', 'product_name', 'category', 'price')
df.show()