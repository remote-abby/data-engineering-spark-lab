from pyspark.sql import SparkSession 
from pyspark.sql import functions as F
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("latestOrder").getOrCreate()

orders = spark.read.csv('/app/datasets/ecommerce/orders.csv', header=True)
orders = orders.filter(F.col('status')=='COMPLETED')

cust_window = Window.partitionBy("customer_id")
orders = orders.withColumn("latest_order", F.max(F.col('order_date')).over(cust_window))
orders.filter(F.col('order_date')==F.col('latest_order')).select('customer_id','order_id','latest_order').distinct().show()