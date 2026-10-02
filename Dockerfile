FROM apache/spark-py:latest

USER 0

RUN pip install --no-cache-dir boto3 botocore

USER 185