from airflow.models import DAG
from datetime import datetime
import time
import random
from airflow.operators.python_operator import PythonOperator

def run_1(ti):
    val = random.randint(10, 30)
    ti.xcom_push(key='value_1', value=val)

def run_2(ti):
    run_1_val = ti.xcom_pull(key='value_1', task_ids='run_1')
    val = run_1_val * 5
    if random.random() > 0.5:
        raise
    ti.xcom_push(key='answer', value=val)

def run_3(ti):
    run_1_val = ti.xcom_pull(key='value_3', task_ids='run_1')
    val = run_1_val * 10
    ti.xcom_push(key='answer', value=val)

def run_4(ti):
    answers = ti.xcom_pull(key='value', task_ids=['run_2', 'run_3'])
    print("answers")

with DAG(
    'MyDAG-1', 
    start_date=datetime(2019, 12, 30),
    schedule = '*/5 * * * *',
    catchup=False
) as dag:
    
    run_1 = PythonOperator(
        task_id='run_1',
        provide_context= True,
        python_callable = run_1,
    )

    run_2 = PythonOperator(
        task_id='run_2',
        provide_context= True,
        python_callable = run_2,
    )

    run_3 = PythonOperator(
        task_id='run_1',
        provide_context= True,
        python_callable = run_1,
    )

    run_4 = PythonOperator(
        task_id='run_2',
        provide_context= True,
        python_callable = run_2,
    )

    # Now, we set the dependencies downstream and, using a list of tasks, our parallel tasks dependency before last_task
    run_1 >> [run_2, run_3] >> run_4