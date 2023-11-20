from airflow import DAG
import pendulum
import datetime
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_with_macro_eg2",
    schedule = "10 0 * * 6#2", # 매월 둘째주 토요일 batch
    start_date = pendulum.datetime(2023, 10, 1, tz='Asia/Seoul'),
    catchup = False,
) as dag:
    
    # start_date: 2주전 월요일, end_date: 2주전 토요일
    bash_task_2 = BashOperator(
        task_id = 'bash_task_2',
        env={'START_DATE':'{{ (data_interval_end.in_timezone("Asia/Seoul") - macros.dateutil.relativedelta.relativedelta(days=19)) | ds}}',
            'END_DATE':'{{ (data_interval_end.in_timezone("Asia/Seoul") - macros.dateutil.relativedelta.relativedelta(days=14)) | ds}}'
        },
        bash_command='echo "START_DATE: $START_DATE" && echo "END_DATE: $END_DATE"'
    )