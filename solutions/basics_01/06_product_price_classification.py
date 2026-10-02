from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder.appName("classify").getOrCreate()

df = spark.read.csv('/app/datasets/ecommerce/products.csv', header=True)
df.withColumn("classified", F.when(F.col('price')<100, F.lit("Budget")).when(F.col('price')<250, 'Standard').otherwise(F.lit('Premium'))).show()