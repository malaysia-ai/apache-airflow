from airflow.models import Variable
from airflow.models import DAG
from datetime import datetime
import time
import random
from airflow.operators.python_operator import PythonOperator, PythonVirtualenvOperator

dag = DAG(
    dag_id='EXAMPLE-virtualenv-mongo',
    start_date=datetime(2019, 12, 30),
    catchup=False,
    schedule = '*/10 * * * *',
)

def callable_virtualenv():
    from pymongo.mongo_client import MongoClient
    from pymongo.server_api import ServerApi

    username = Variable.get('mongodb-user')
    password = Variable.get('mongodb-password')
    uri = f"mongodb+srv://{username}:{password}@cluster0.ntovpqz.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(uri, server_api=ServerApi('1'))
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

PythonVirtualenvOperator(
    task_id="callable_virtualenv_task",
    requirements="pymongo",
    python_callable=callable_virtualenv,
    dag=dag,
)