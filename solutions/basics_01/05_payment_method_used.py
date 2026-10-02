from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder.appName("paymentMethods").getOrCreate()

df = spark.read.csv('/app/datasets/ecommerce/payments.csv', header=True)

df.select(F.col('payment_method')).distinct().show()