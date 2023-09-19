from airflow.models import DAG
from datetime import datetime
import time
import random
from airflow.operators.python_operator import PythonOperator


dag = DAG(
    dag_id='EXAMPLE-python',
    start_date=datetime(2019, 12, 30),
    catchup=False,
    schedule = '*/5 * * * *',
)

def run(i, **kwargs):
    # simulate long IO
    time.sleep(random.randint(1, 30))
    if random.random() > 0.5:
        raise
    print(f'run {i}')

def second_run(k, **kwargs):
    # simulate long IO
    time.sleep(random.randint(10, 30))
    print(f'second_run {k}')


for i in range(10):
    run_task = PythonOperator(
        task_id=f'run_{i}',
        python_callable = run,
        op_kwargs = {'i' : i},
        dag=dag,
    )
    second_run_task = PythonOperator(
        task_id=f'second_run_{i}',
        python_callable = second_run,
        op_kwargs = {'k' : i},
        dag=dag,
    )
    run_task.set_downstream(second_run_task)
