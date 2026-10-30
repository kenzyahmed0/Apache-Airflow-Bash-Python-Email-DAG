from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.email import EmailOperator
from datetime import datetime, timedelta

with DAG(
    dag_id='dag7',
    start_date=datetime(2026, 10, 30),
    schedule_interval=timedelta(minutes=5),
    catchup=False
) as dag:

    task1 = BashOperator(
        task_id='task1',
        bash_command="echo 'Pipeline started'"
    )

    task2 = BashOperator(
        task_id='task2',
        bash_command="python /data/app.py"
    )

    task3 = EmailOperator(
        task_id="send_email",
        to='safehec418@moblha.com;distantbabygirl@gmail.com',
        subject='Test Airflow',
        html_content="<h3>Pipeline finished</h3>"
    )

    task1 >> task2 >> task3
    