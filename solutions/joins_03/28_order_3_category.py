from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder.appName("diffCat").getOrCreate()

orders = spark.read.csv('/app/datasets/ecommerce/orders.csv', header=True)
order_items = spark.read.csv('/app/datasets/ecommerce/order_items.csv', header=True)
customers = spark.read.csv('/app/datasets/ecommerce/customers.csv', header=True)
products = spark.read.csv('/app/datasets/ecommerce/products.csv', header=True)

customer_order = customers.join(orders, on='customer_id', how="inner")
cust_oi_df = customer_order.join(order_items, on='order_id', how="inner")
all_details = cust_oi_df.join(products, on='product_id', how="inner")

all_details.show()

# customer_name, order_id, categories, total_amount
all_details = all_details.withColumn("customer_name", F.initcap(F.concat_ws(" ", F.col('first_name'), F.col('last_name'))))
all_details = all_details.groupby('order_id','customer_name','total_amount').agg(F.count_distinct(F.col("category")).alias("catCount"))
all_details.show()
all_details.filter(F.col('catCount')>=3).show()
