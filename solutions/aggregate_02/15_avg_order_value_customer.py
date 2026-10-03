from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder.appName("avgOrderValue").getOrCreate()

orders = spark.read.csv('/app/datasets/ecommerce/orders.csv', header=True)
customers = spark.read.csv('/app/datasets/ecommerce/customers.csv', header=True)
customers = customers.select("customer_id")
orders = orders.filter(F.col("status")=='COMPLETED')
avg_order = orders.groupby("customer_id").agg(F.avg(F.col('total_amount')).alias("avg_spending"))
avg_order = avg_order.withColumn("avg_spending", F.round("avg_spending",2))
customers.join(avg_order, how="left", on="customer_id").show()