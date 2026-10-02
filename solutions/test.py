from pyspark.sql import SparkSession
from boto3 import client

sc = SparkSession.builder.appName("Sparky").getOrCreate()

print('spark version :',sc.version)

client = client('s3')
print('s3 client :',client)