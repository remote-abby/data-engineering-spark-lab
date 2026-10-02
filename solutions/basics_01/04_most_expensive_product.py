from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("mostExpensive").getOrCreate()

wind = Window.partitionBy()
df = spark.read.csv('/app/datasets/ecommerce/products.csv', header=True)
df.withColumn("MaxPrice", F.max("price").over(wind)).filter(F.col("price")==F.col("MaxPrice")).drop("MaxPrice").show()
