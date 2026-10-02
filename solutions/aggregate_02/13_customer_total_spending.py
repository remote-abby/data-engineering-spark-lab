from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder.appName("CustomerSpend").getOrCreate()

df = spark.read.csv('/app/datasets/ecommerce/orders.csv', header=True)
success_orders = df.filter(F.col('status')=='COMPLETED')
success_orders.groupby(F.col("customer_id")).agg(F.sum(F.col("total_amount")).alias('total_spend')).show()