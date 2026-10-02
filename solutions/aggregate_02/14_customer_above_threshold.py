from pyspark.sql import SparkSession, functions as F, window

spark = SparkSession.builder.appName("CustomerSpend").getOrCreate()

df = spark.read.csv('/app/datasets/ecommerce/orders.csv', header=True)
success_orders = df.filter(F.col('status')=='COMPLETED')
all_customers = success_orders.groupby(F.col("customer_id")).agg(F.sum(F.col("total_amount")).alias('total_spend'))

wind = window.Window.partitionBy()

all_customers.withColumn("avg_spend", F.avg("total_spend").over(wind)) \
.filter(F.col("total_spend")>F.col("avg_spend")) \
.select("customer_id", "total_spend").show()