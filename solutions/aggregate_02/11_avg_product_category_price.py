from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("avg_category").getOrCreate()

df = spark.read.csv('/app/datasets/ecommerce/products.csv', header=True)

df.groupby('category').agg(F.avg('price').alias("category_count")).show()