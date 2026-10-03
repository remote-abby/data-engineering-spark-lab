from pyspark.sql import SparkSession, functions as F, window

spark = SparkSession.builder.appName("percentage").getOrCreate()

payments = spark.read.csv('/app/datasets/ecommerce/payments.csv', header=True)

payments = payments.groupby('payment_status').agg(F.count('*').alias('total_count'))
globalwind = window.Window().partitionBy()
pay = payments.withColumn('percentage', F.col('total_count')*100/F.sum('total_count').over(globalwind))
pay = pay.withColumn("percentage", F.concat(F.round("percentage",2),F.lit("%")))
pay.filter(F.col('payment_status')=='SUCCESS').drop("total_count").show()