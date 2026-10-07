from pyspark.sql import SparkSession, functions as F, window

spark = SparkSession.builder.appName("abouveAvg").getOrCreate()

customers = spark.read.csv('/app/datasets/ecommerce/customers.csv', header=True)
orders = spark.read.csv('/app/datasets/ecommerce/orders.csv', header=True)

orders = orders.filter(F.col('status')=='COMPLETED')
cust_ord = customers.join(orders, on='customer_id', how='left')
cust_ord.show()
globwin = window.Window.partitionBy()
cust_ord.groupby('customer_id').agg(F.sum(F.col('total_amount')).alias('customer_spending')).withColumn('AvgSpending', F.avg(F.col('customer_spending')).over(globwin)).filter(F.col('customer_spending')>=F.col('AvgSpending')).show()