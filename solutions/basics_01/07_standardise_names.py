from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder.appName("standardize").getOrCreate()

df = spark.read.csv('/app/datasets/ecommerce/customers.csv', header=True)

df.withColumn("name", F.initcap(F.concat_ws(" ",F.trim(F.col('first_name')), F.trim(F.col('last_name'))))).select('name').show()