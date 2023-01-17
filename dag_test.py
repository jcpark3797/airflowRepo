from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.operators.bash_operator import BashOperator

from datetime import datetime

dag = DAG(
    'docker_dag',
    schedule_interval="0 0 * * 1",
    start_date=datetime(2020, 10, 19),
    catchup=False
)

def print_hello():
    return 'Hello world!'

start = DummyOperator(task_id='start', dag=dag)

end = DummyOperator(task_id='end', dag=dag)

job1 = PythonOperator(
    task_id='hello_task',
    dag=dag,
    python_callable=print_hello)

job2 = BashOperator(
    task_id='echo_test',
    bash_command='echo 1',
)

job3 = BashOperator(
    task_id='run_after_loop',
    bash_command='/my_spark/test.sh ',
)

start >> job1 >> job2 >> job3 >> end
