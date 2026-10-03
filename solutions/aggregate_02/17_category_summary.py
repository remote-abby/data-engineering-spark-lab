
# For every product category, calculate:
# 1. The total number of products in the category. - done
# 2. The number of distinct products that have actually
#    been sold.
# 3. The total quantity of products sold.

from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder.appName("catSummary").getOrCreate()

products = spark.read.csv('/app/datasets/ecommerce/products.csv', header=True)
order_items = spark.read.csv('/app/datasets/ecommerce/order_items.csv', header=True)

products.groupby('category').agg(F.count('*').alias('cat_count')).show()
order_items.groupby('product_id').agg(F.sum('quantity').alias('prod_sold')).select('product_id','prod_sold').show()
order_items.agg(F.count_distinct('product_id').alias('uniq_prod_sold')).select('uniq_prod_sold').show()