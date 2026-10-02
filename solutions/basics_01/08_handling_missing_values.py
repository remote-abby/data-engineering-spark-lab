from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder.appName("handleNull").getOrCreate()

df = spark.read.csv('/app/datasets/ecommerce/customers.csv', header=True)

df.withColumn("email", F.coalesce(F.expr("nullif(trim(email), '')"), F.lit("UNKNOWN"))).select("customer_id", "email").show()