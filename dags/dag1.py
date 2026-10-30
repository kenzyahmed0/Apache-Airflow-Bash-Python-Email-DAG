# bash operator
# python operator
# mail operator

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.operators.email import EmailOperator
from datetime import datetime, timedelta

# bash operator
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

with DAG(
    dag_id='dag1',
    start_date=datetime(2026, 10, 30),
    schedule_interval=timedelta(minutes=5),
    catchup=False
) as dag:

    task1 = BashOperator(
        task_id='task1',
        bash_command="echo 'My name is Kenzy Ahmed'"
    )

    task2 = BashOperator(
        task_id='task2',
        bash_command="date"
    )

    task3 = BashOperator(
        task_id='task3',
        bash_command="pwd"
    )

    task1 >> task3 >> task2