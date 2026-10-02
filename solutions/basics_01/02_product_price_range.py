
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName('PriceBetween').getOrCreate()

df = spark.read.csv('/app/datasets/ecommerce/products.csv', header=True)
df.show()
products = df.filter(F.col('price').between(10, 100)) 
products.show()
