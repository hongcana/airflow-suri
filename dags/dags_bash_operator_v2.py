
import datetime
import pendulum
import logging

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.decorators import task

@task # PythonOperattor 대체
def bash_t1():
    logging.info("========= bash_t1 start. =========")
    print("hello world!")
    return "hello world!"




with DAG(
    dag_id="dags_bash_operator_v2", # 파이썬 파일명과 일치 권고
    schedule="0 * * * *", # Cron 스케줄 - 분, 시, 일, 월, 요일로 읽는다.
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"), # DAG의 시작 날짜. timezone이 UTC로 두면 9시간 늦게 돌음.
    catchup=False, # Backfill(이전에 실행되지 않은 작업을 돌리는 것)을 할 것인지 여부
    #dagrun_timeout=datetime.timedelta(minutes=60), # 60분 이상 돌면 실패
    # tags=["hongcana_exmample"], # 해쉬태그 설정(optional)
    # params={"example_key": "example_value"}, # task들에 공통적으로 넘겨줄 파라미터(optional)
) as dag:
    
    bash_t2 = BashOperator(
        task_id = "bash_t2",
        bash_command= "echo $HOSTNAME",
    )
    # Assign the tasks to the DAG in order
    bash_t1() >> bash_t2
