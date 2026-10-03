from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder.appName('catMed').getOrCreate()

products = spark.read.csv('/app/datasets/ecommerce/products.csv', header=True)

products.groupby('category').agg(F.median('price')).show()