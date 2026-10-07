from pyspark.sql import SparkSession, functions as F, window

spark = SparkSession.builder.appName("aboveCatAvg").getOrCreate()

products = spark.read.csv('/app/datasets/ecommerce/products.csv', header=True)

prodWin = window.Window.partitionBy('category')
products.withColumn("prod_Avg", F.avg(F.col('price')).over(prodWin)).filter(F.col('price')>F.col('prod_Avg')).show()