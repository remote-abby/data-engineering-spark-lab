from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder.appName("monthlyRevenue").getOrCreate()

df = spark.read.csv('/app/datasets/ecommerce/orders.csv', header=True)
orders = df.withColumn("year_month", F.date_format(F.col('order_date'), 'yyyy-MM')).filter(F.col('status')=='COMPLETED')
orders.groupby(F.col("year_month")).agg(F.sum(F.col('total_amount'))).show()