from airflow.models import DAG
from datetime import datetime
import time
import random
from airflow.operators.python_operator import PythonOperator
import pyspark
import os
from pyspark.sql import SparkSession

dag = DAG(
    dag_id='EXAMPLE-pyspark',
    start_date=datetime(2019, 12, 30),
    catchup=False,
    schedule = '*/5 * * * *',
)

def run(**kwargs):
    print(os.getenv('SPARK_MASTER_HOST'))
    # spark = SparkSession.builder.master(os.getenv('SPARK_MASTER_HOST', 'local')).getOrCreate()

    spark = SparkSession.builder.appName("App").master(os.getenv('SPARK_MASTER_HOST', 'local')) \
            .config("spark.executor.memory", "2g") \
            .config("spark.driver.memory", "2g") \
            .getOrCreate()

    cores = spark._jsc.sc().getExecutorMemoryStatus().keySet().size()
    appid = spark._jsc.sc().applicationId()
    print("You are working with", cores, "core(s) on appid: ",appid)


    values = [("data_1", 1, 2, 3),
            ("data_2", 4, 5, 6),
            ("data_3", 7, 8, 9),
            ("data_4", 10, 11, 12)]

    df = spark.createDataFrame(values, ["column_name_1", "column_name_2", "column_name_3", "column_name_4"])

    sum_result = df.selectExpr("sum(column_name_2)").collect()[0][0]
    print(f"Sum of column_name_2: {sum_result}")
    df.show()

run_task = PythonOperator(
        task_id='run',
        python_callable = run,
        # queue = "kubernetes", #run in kubernetes pod
        dag=dag,
    )



